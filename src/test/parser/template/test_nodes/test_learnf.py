import xml.etree.ElementTree as ET

from programy.parser.template.nodes.base import TemplateNode
from programy.parser.template.nodes.learnf import TemplateLearnfNode
from programy.parser.template.nodes.word import TemplateWordNode
from programy.config.brain import BrainFileConfiguration

from test.parser.template.base import TemplateTestsBaseClass


class TemplateLearnfNodeTests(TemplateTestsBaseClass):

    def test_node(self):
        root = TemplateNode()
        self.assertIsNotNone(root)

        learn = TemplateLearnfNode()
        self.assertIsNotNone(learn)
        learn._pattern = ET.fromstring("<pattern>HELLO LEARN</pattern>")
        learn._topic = ET.fromstring("<topic>*</topic>")
        learn._that = ET.fromstring("<that>*</that>")
        learn._template = TemplateWordNode("LEARN")

        root.append(learn)
        self.assertEqual(1, len(root.children))

        self.bot.brain._configuration._aiml_files = BrainFileConfiguration("/tmp", ".aiml", False)

        resolved = root.resolve(self.bot, self.clientid)
        self.assertIsNotNone(resolved)
        self.assertEqual("", resolved)

    def test_to_xml(self):
        root = TemplateNode()
        learn = TemplateLearnfNode()
        learn._pattern = ET.fromstring("<pattern>HELLO LEARN</pattern>")
        learn._topic = ET.fromstring("<topic>*</topic>")
        learn._that = ET.fromstring("<that>*</that>")
        learn._template = TemplateWordNode("LEARN")
        root.append(learn)

        xml = root.xml_tree(self.bot, self.clientid)
        self.assertIsNotNone(xml)
        xml_str = ET.tostring(xml, "utf-8").decode("utf-8")
        self.assertEqual("<template><learnf><pattern>HELLO LEARN</pattern><topic>*</topic><that>*</that><template>LEARN</template></learnf></template>", xml_str)


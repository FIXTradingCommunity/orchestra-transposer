import os

from orchestratransposer import Unified2Orchestra, Unified

XML_FILE_DIR = os.path.join(os.path.dirname(__file__), 'xml/')


def output_dir():
    path = os.path.join(os.path.dirname(__file__), 'out/')
    os.makedirs(path, exist_ok=True)
    return path


def test_unified2orchestra_xml():
    xml_path = os.path.join(XML_FILE_DIR, 'FixRepository.xml')
    phrases_xml_path = os.path.join(XML_FILE_DIR, 'FixPhrases.xml')
    output_path = os.path.join(output_dir(), 'FixRepository2Orchestra.xml')
    translator = Unified2Orchestra()
    with open(output_path, 'wb') as f:
        errors = translator.unified2orch_xml(xml_path, phrases_xml_path, f)
        assert not errors


def test_unified2orchestra_dict():
    xml_path = os.path.join(XML_FILE_DIR, 'FixRepository.xml')
    phrases_xml_path = os.path.join(XML_FILE_DIR, 'FixPhrases.xml')
    output_path = os.path.join(output_dir(), 'FixRepository2Orchestra-dict.txt')
    unified = Unified()
    (unified_instance, errors) = unified.read_xml_all(xml_path, phrases_xml_path)
    assert not errors
    translator = Unified2Orchestra()
    orch_instance = translator.unified2orch_dict(unified_instance, "OrchestraFIXLatest")
    with open(output_path, 'w') as f:
        print(str(orch_instance), file=f)

import os

from orchestratransposer import Unified
from orchestratransposer.unified.unified import UnifiedMain, UnifiedPhrases

XML_FILE_DIR = os.path.join(os.path.dirname(__file__), 'xml/')


def output_dir():
    path = os.path.join(os.path.dirname(__file__), 'out/')
    os.makedirs(path, exist_ok=True)
    return path


def test_valid():
    unified = UnifiedMain()
    xml_path = os.path.join(XML_FILE_DIR, 'FixRepository.xml')
    errors = unified.validate(xml_path)
    assert not errors


def test_to_fix_version_dict():
    unified = UnifiedMain()
    xml_path = os.path.join(XML_FILE_DIR, 'FixRepository.xml')
    output_path = os.path.join(output_dir(), 'FixRepository-fix-dict.txt')
    with open(output_path, 'w') as f:
        (instance, errors) = unified.read_xml(xml_path)
        assert not errors
        fix = instance.fix("FIX.Latest_EP269")
        print(str(fix), file=f)


def test_to_fix_no_version_dict():
    unified = UnifiedMain()
    xml_path = os.path.join(XML_FILE_DIR, 'FixRepository.xml')
    output_path = os.path.join(output_dir(), 'FixRepository-fix-dict.txt')
    with open(output_path, 'w') as f:
        (instance, errors) = unified.read_xml(xml_path)
        assert not errors
        fix = instance.fix()
        print(str(fix), file=f)


def test_phrases_valid():
    unified = UnifiedPhrases()
    xml_path = os.path.join(XML_FILE_DIR, 'FixPhrases.xml')
    errors = unified.validate(xml_path)
    assert not errors


def test_phrases_to_dict():
    unified = UnifiedPhrases()
    xml_path = os.path.join(XML_FILE_DIR, 'FixPhrases.xml')
    output_path = os.path.join(output_dir(), 'FixPhrases-dict.txt')
    with open(output_path, 'w') as f:
        (instance, errors) = unified.read_xml(xml_path)
        instance.append_documentation('FIELD_9999', [('SYNOPSIS', 'Test documentation'),
                                                     ('ELABORATION', 'Even more documentation')])
        print(str(instance), file=f)
        assert not errors
        assert instance.text_id('FIELD_2217') == [('SYNOPSIS', ['The fee amount due if different from MiscFeeAmt(137).'])]
        assert instance.text_id('FIELD_9999') == [('SYNOPSIS', ['Test documentation']),
                                                  ('ELABORATION', ['Even more documentation'])]


def test_text_id():
    unified = UnifiedPhrases()
    xml_path = os.path.join(XML_FILE_DIR, 'FixPhrases.xml')
    (instance, errors) = unified.read_xml(xml_path)
    assert not errors
    t = instance.text_id('FIELD_41163')
    assert t == [
        ('SYNOPSIS', ['The occurrence of the day of week on which fixing takes place.']),
        ('ELABORATION',
         ['For example, a fixing of the 3rd Friday would be DayOfWk=5 DayNum=3. If omitted every day of the week is a fixing day.'])]


def test_to_dict():
    unified = UnifiedMain()
    xml_path = os.path.join(XML_FILE_DIR, 'FixRepository.xml')
    output_path = os.path.join(output_dir(), 'FixRepository-dict.txt')
    with open(output_path, 'w') as f:
        (instance, errors) = unified.read_xml(xml_path)
        print(str(instance), file=f)
        assert not errors


def test_to_from_dict():
    unified = UnifiedMain()
    xml_path = os.path.join(XML_FILE_DIR, 'FixRepository.xml')
    output_path = os.path.join(output_dir(), 'FixRepository-copy.xml')
    with open(output_path, 'wb') as f:
        (instance, errors) = unified.read_xml(xml_path)
        unified.write_xml(instance, f)
        assert not errors


def test_unified_to_dict():
    unified = Unified()
    xml_path = os.path.join(XML_FILE_DIR, 'FixRepository.xml')
    phrases_xml_path = os.path.join(XML_FILE_DIR, 'FixPhrases.xml')
    output_path = os.path.join(output_dir(), 'FixRepository-phrases-dict.txt')
    with open(output_path, 'w') as f:
        (instance, errors) = unified.read_xml_all(xml_path, phrases_xml_path)
        print(str(instance), file=f)
        assert not errors

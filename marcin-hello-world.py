import csv
import json
from xml.etree import ElementTree

translation = {39: None}

input_file = 'plik.xml'
output_file = 'output_test.csv'

header_list = ('Summary', 'Assignee', 'Reporter', 'Issue Type', 'Description', 'Test Type', 'Manual Test Steps')


def convert_to_csv():
    tree = ElementTree.parse(input_file)
    root = tree.getroot()
    write_csv(root)


def write_csv(root):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header_list)
        for testcase in root.iter('testcase'):
            row = get_row(testcase)
            writer.writerow(row)


def get_row(testcase):
    steps_array = []
    index = 0
    testcase_name = testcase.attrib['name']
    for step in testcase.iter('step'):
        set_step(index, step, steps_array)
    return [testcase_name, "183503", "183503", "13900", testcase_name, "Manual",
            str(steps_array).translate(translation)]


def set_step(index, step, steps_array):
    final_action = step.find('actions').text
    expected_result = step.find('expectedresults').text
    step = convert_to_json(index, final_action, None, expected_result)
    steps_array.append(step)
    index += 1


def convert_to_json(index, step, required_data, result):
    data = {'index': index, 'step': step, 'data': required_data, 'result': result}

    json_object = json.dumps(data, ensure_ascii=False)

    return json_object


if __name__ == "__main__":
    convert_to_csv()
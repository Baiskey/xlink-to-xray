from xml.etree import ElementTree
import csv

translation = {39: None}

def print_xml():
    row_list = ["Summary", "Assignee", "Reporter", "Issue Type", "Description", "Test Type", "Manual Test Steps"]
    tree = ElementTree.parse("plik.xml")
    root = tree.getroot()

    with open('output_test.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        # csv.writer(fileobj, quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
        writer.writerow(row_list)
        for testcase in root.iter('testcase'):
            steps_array = []
            index = 0
            testcase_name = testcase.attrib['name']
            print("Name: " + testcase_name)
            for step in testcase.iter('step'):
                final_action = step.find('actions').text.replace('"', '')
                expected_result = step.find('expectedresults').text.replace('"', '')
                print("Action:" + final_action)
                print("Expected result: " + expected_result)
                steps_array.append(prepare_execution_step(index, final_action, None, expected_result))
                index += 1
            # print("\n\n\n Printing steps array: " + str(steps_array).translate(translation))
            steps_array_in_string = str(steps_array).translate(translation)
            writer.writerow([testcase_name, "183503", "183503", "13900", testcase_name, "Manual", steps_array_in_string])
            print("\n")


def prepare_execution_step(index, step, required_data, result):
    template = '"index": {}, "step": "{}", "data": "{}", "result": "{}"'.format(index, step,
                                                                                              required_data, result)
    return '{' + template + '}'


if __name__ == "__main__":
    # print(prepare_execution_step(0, "Hello World", "nothing", "expected result"))
    print_xml()

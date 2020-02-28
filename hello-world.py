from xml.etree import ElementTree
import os
import csv


def print_xml():
    row_list = ["Summary", "Assignee", "Reporter", "Issue Type", "Description", "Test Type", "Manual Test Steps"]
    tree = ElementTree.parse("test.xml")
    root = tree.getroot()

    with open('output_test.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(row_list)
        for testcase in root.iter('testcase'):
            steps_array = []
            index = 0
            testcase_name = testcase.attrib['name']
            print("Name: " + testcase_name)
            for step in testcase.iter('step'):
                final_action = step.find('actions').text
                expected_result = step.find('expectedresults').text
                print("Action:" + final_action)
                print("Expected result: " + expected_result)
                steps_array.append(prepare_execution_step(index, final_action, "", expected_result))
                index += 1
            writer.writerow([testcase_name, "183503", "183503", "10000", testcase_name, "Manual", str(steps_array)])
            # print(steps_array)
            print("\n")


def prepare_execution_step(index, step, required_data, result):
    template = '""index"": {}, ""step"": ""{}"", ""data"": ""{}"", ""result"": ""{}""'.format(index, step,
                                                                                              required_data, result)
    return '{' + template + '}'


if __name__ == "__main__":
    # print(prepare_execution_step(0, "Hello World", "nothing", "expected result"))
    print_xml()

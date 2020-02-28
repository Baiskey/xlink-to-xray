from xml.etree import ElementTree
import os
import csv


def print_xml():
    row_list = ["Summary", "Assignee", "Reporter", "Issue Type", "Description", "Test Type", "Manual Test Steps"]
    tree = ElementTree.parse("test.xml")
    root = tree.getroot()

    with open('output_test.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        for testcase in root.iter('testcase'):
            print("Name: " + testcase.attrib['name'])
            for step in testcase.iter('step'):
                final_action = step.find('actions').text
                expected_result = step.find('expectedresults').text
                print("Action:" + final_action)
                print("Expected result: " + expected_result)
            print("\n")


def prepare_execution_step(index, step, required_data, result):
    template = '""index"": {}, ""step"": ""{}"", ""data"": ""{}"", ""result"": ""{}""'.format(index, step,
                                                                                              required_data, result)
    return '{' + template + '}'


if __name__ == "__main__":
    print(prepare_execution_step(0, "Hello World", "nothing", "expected result"))
    # print_xml()

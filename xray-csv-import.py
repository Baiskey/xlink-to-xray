from xml.etree import ElementTree
import csv

def print_xml():
    row_list = ["TCID","Test Summary", "Test Priority", "Step", "Data", "Result"]
    tree = ElementTree.parse("plik.xml")
    root = tree.getroot()

    with open('output_test.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(row_list)
        # TCID, Test Summary, Test Priority, Step Data, Result
        index = 1
        for testcase in root.iter('testcase'):
            steps_array = []
            testcase_name = testcase.attrib['name']
            print("Name: " + testcase_name)
            writer.writerow([index, testcase_name, "High", "", "", ""])
            for step in testcase.iter('step'):
                final_action = step.find('actions').text.replace('"', '')
                expected_result = step.find('expectedresults').text.replace('"', '')
                print("Action:" + final_action)
                print("Expected result: " + expected_result)
                writer.writerow([index, "", "", final_action, "", expected_result])
            index += 1
            print("\n")


def prepare_execution_step(index, step, required_data, result):
    template = '"index": {}, "step": "{}", "data": "{}", "result": "{}"'.format(index, step,
                                                                                              required_data, result)
    return '{' + template + '}'


if __name__ == "__main__":
    # print(prepare_execution_step(0, "Hello World", "nothing", "expected result"))
    print_xml()

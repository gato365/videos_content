import os
import re

# Function to read and split main Quarto file content
def split_quarto_content(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Example regex pattern to split the document into sections
    # This needs to be customized based on your document's structure
    sections = re.split(r'<!-- SECTION: ([\w\s\(\)]+) -->', content)
    
    # Create a dictionary to hold content for each section
    section_content = {}
    for i in range(1, len(sections), 2):
        section_name = sections[i]
        section_data = sections[i + 1]
        section_content[section_name] = section_data
    
    return section_content
    

# Function to write content to specific directories and files
# Function to write content to specific directories and files
def distribute_content(content_dict, base_dir='.', yaml_path='theyaml.yml'):
    # Read YAML content to prepend to each file
    with open(yaml_path, 'r', encoding='utf-8') as yaml_file:
        yaml_content = yaml_file.read()
    
    for section_name, data in content_dict.items():
        # Extract section number from section_name
        section_number = int(re.search(r'\d+', section_name).group())
        
        # Define file paths based on section name
        answer_key_path = os.path.join(base_dir, section_name, 'answer-key.qmd')
        student_version_path = os.path.join(base_dir, section_name, 'student-version.qmd')
        fill_in_version_path = os.path.join(base_dir, section_name, 'fill_in-version.qmd')
        
        # Ensure directory exists for section 6 and above
        if section_number >= 6:
            os.makedirs(os.path.dirname(answer_key_path), exist_ok=True)
        
        # Write the same content to all versions for this example
        # In a real scenario, you would customize content per file
        for path in [answer_key_path, student_version_path, fill_in_version_path]:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(yaml_content + '\n' + data)





# Main logic
if __name__ == "__main__":
    main_quarto_path = 'mainquarto.qmd'
    content_dict = split_quarto_content(main_quarto_path)
    
    
    distribute_content(content_dict)




from PyPDF2 import PdfReader
import re
import sys 

def change(file_name, output_file, word_to_change, word_to, end = 0 , start = 1):
    reader = PdfReader(file_name)
    if end == 0:
      end = len(reader.pages)
    word = re.compile(re.escape(word_to_change), re.IGNORECASE)
    text_changed = ''
    
    output_file = open(output_file, 'w+')
    output_file.truncate(0)

    for i in range(start - 1, end): 
        page = reader.pages[i]
        text = page.extract_text()
        text_changed = word.sub(word_to, text)
        lines = text_changed.splitlines()
        output_file.write('\n'.join(lines))
        output_file.write('\n\n\n')
        print(f"Readed page number {i + 1}")

if len(sys.argv) == 7:
  change(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5]), int(sys.argv[6]))
elif len(sys.argv) == 6:
  change(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5]))
elif len(sys.argv) == 5:
  change(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
else:
  # from_file: the file you want to change the word
  # to_file: the file wich will save the text with the changed word
  # word: the word you want to change
  # word_to: the word you want
  # end_page: from_file page you want to finish = len(from_file.pages) by default
  # start_page: from_file page you want to start = 0 by default
  change(from_file, to_file, word, word_to, end_page, start_page)
def main():
  book_path = './books/frankenstein.txt'
  text = read_book(book_path)
  word_count = count_words(text)
  characters = count_characters(text)
  list__characters = list(characters.items())
  count_alpha = filter_letters(list__characters)
  build_report(word_count, count_alpha)

def read_book(book_path):
  with open(book_path) as f:
    return f.read()

def count_words(text):
  word_count = len(text.split())
  return word_count

def count_characters(text):
  lower_text = text.lower()
  letters = {}
  for letter in lower_text:
    if letter in letters:
      letters[letter] += 1
    else:
      letters[letter] = 1
  return letters

def filter_letters(count_characters):
  count_alpha = []
  for i in range(0, len(count_characters)):
    if count_characters[i][0].isalpha():
      count_alpha.append(count_characters[i])
  return sorted(count_alpha, key = lambda x: x[1], reverse=True)

def build_report(word_count, count_alpha):
  print(f'{word_count} words found in the document')
  for i in range(0, len(count_alpha)):
    print(f'The {count_alpha[i][0]} character was found {count_alpha[i][1]} times')

main()
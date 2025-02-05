from file_utils.text_processor import count_words

def main():
    file_path = input("단어 수를 셀 텍스트 파일의 경로를 입력하세요: ")
    word_count = count_words(file_path)
    print(f"파일의 단어 수: {word_count}")

if __name__ == '__main__':
    main()
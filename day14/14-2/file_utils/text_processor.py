def count_words(file_path):
    """지정한 텍스트 파일의 단어 수를 세어 반환합니다."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        words = text.split()
        return len(words)
    except Exception as e:
        print(f"파일 읽기 에러: {e}")
        return 0
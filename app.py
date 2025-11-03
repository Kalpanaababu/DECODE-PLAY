from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# --- Chest 1: Vowel Twist Logic ---
def voweltwist(s):
    vowels = 'aeiouAEIOU'
    result = ''
    for i, ch in enumerate(s):
        if ch in vowels:
            if ch.islower():
                result += chr(((ord(ch) - 97 + (i + 1)) % 26) + 97)
            else:
                result += chr(((ord(ch) - 65 + (i + 1)) % 26) + 65)
        elif ch.isalpha():
            result += ch.lower() if ch.isupper() else ch.upper()
        else:
            result += ch
    return result


@app.route('/voweltwist', methods=['POST'])
def vowel_twist_route():
    try:
        text = request.form.get('input_text', '')
        output = voweltwist(text)
        hint = "HINT: The way a letter transforms depends on what it is and where it stands."
        return jsonify({'result': output, 'hint': hint})
    except Exception as e:
        return jsonify({'result': f'Error: {str(e)}', 'hint': ''})


# --- Chest 2: Binary Glow Logic ---
def binary_glow(numbers):
    result = []
    for num in numbers:
        binary = bin(int(num))[2:]
        ones = binary.count('1')
        pattern = str(ones) * ones
        result.append(pattern)
    return result


@app.route('/binaryglow', methods=['POST'])
def binary_glow_route():
    try:
        nums_str = request.form.get('numbers', '[]')
        nums = json.loads(nums_str)
        output = binary_glow(nums)
        hint = "HINT: Every number glows differently in binary form."
        return jsonify({'result': output, 'hint': hint})
    except Exception as e:
        return jsonify({'result': [f'Error: {str(e)}'], 'hint': ''})


# --- Chest 3: Matrix Decoder Logic ---
def matrix_decoder(matrix):
    n = len(matrix)
    row_sum = [sum(matrix[i]) for i in range(n)]
    col_sum = [sum(matrix[j][i] for j in range(n)) for i in range(n)]
    decoded = [[row_sum[i] + col_sum[j] - matrix[i][j] for j in range(n)] for i in range(n)]
    return decoded


@app.route('/matrixdecoder', methods=['POST'])
def matrix_decoder_route():
    try:
        data = request.get_json(force=True)
        matrix = data.get('matrix', [])
        result = matrix_decoder(matrix)
        hint = "HINT: Each decoded value blends row and column energy, subtracting its own."
        return jsonify({'result': result, 'hint': hint})
    except Exception as e:
        return jsonify({'result': [[f'Error: {str(e)}']], 'hint': ''})


# --- Chest 4: Decode Stack Challenge Logic ---
def decode_stack(nums):
    n = len(nums)
    stack = []
    for i in range(n):
        if i % 2 == 0:
            stack.append(nums[i])
        else:
            stack.insert(0, nums[i])
        if len(stack) > 3:
            stack.pop()
    return sum(stack)


@app.route('/decodestack', methods=['POST'])
def decode_stack_route():
    try:
        nums_str = request.form.get('numbers', '[]')
        nums = json.loads(nums_str)
        result = decode_stack(nums)
        hint = "HINT: Even ones climb, odd ones sneak to the front — only three survive."
        return jsonify({'result': result, 'hint': hint})
    except Exception as e:
        return jsonify({'result': f'Error: {str(e)}', 'hint': ''})


if __name__ == '__main__':
    app.run(debug=True)

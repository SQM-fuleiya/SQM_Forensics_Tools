from PIL import Image  
  
def extract_lsb(image_path, bytes_to_extract):  
    # 打开图片  
    img = Image.open(image_path)  
    img = img.convert('RGB')  # 确保图片是RGB模式  
    pixels = img.load()  
      
    # 初始化一个空字节串来存储提取的数据  
    extracted_data = bytearray()  
      
    # 遍历图片的每个像素  
    width, height = img.size  
    bit_index = 0  
    byte_index = 0  
    current_byte = 0  
      
    for y in range(height):  
        for x in range(width):  
            r, g, b = pixels[x, y]  
              
            # 从红色通道提取LSB  
            bit = r & 1  
            current_byte |= (bit << (7 - bit_index))  
            bit_index += 1  
              
            # 如果收集了一个完整的字节  
            if bit_index == 8:  
                extracted_data.append(current_byte)  
                  
                # 如果已经提取了足够的字节  
                if byte_index >= bytes_to_extract:  
                    return extracted_data[:bytes_to_extract]  
                  
                current_byte = 0  
                bit_index = 0  
                byte_index += 1  
      
    # 如果图片中没有足够的像素来提取所有字节  
    return extracted_data  
  
# 使用示例  
image_path = 'path_to_your_stego_image.jpg'  
bytes_to_extract = 100  # 假设我们知道需要提取的字节数  
extracted_data = extract_lsb(image_path, bytes_to_extract)  
  
# 将提取的字节转换为字符串（假设是ASCII编码）  
try:  
    extracted_str = extracted_data.decode('ascii')  
    print("Extracted text:", extracted_str)  
except UnicodeDecodeError:  
    print("Extracted data is not valid ASCII text.")
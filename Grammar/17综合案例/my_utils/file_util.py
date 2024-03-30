def print_file_info(file_name):
    global file
    try:
        file= open(file_name, 'r', encoding="UTF-8")
    except Exception as e:
        print(f"文件不存在{e}")
    else:
        content=file.read()
        print(f"文件的内容是:\n{content}")
    finally:
        try:
            file.close()
        except:
            pass
def append_to_file(file_name,data):
    with open(file_name,'a',encoding="UTF-8") as f:
        f.write(data)
        f.close()

if __name__ == '__main__':
    print_file_info('../test.txt')
    append_to_file('../test.txt','\n测试追加的数据')

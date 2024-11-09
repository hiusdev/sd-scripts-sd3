import os

# Thay 'path/to/directory' bằng đường dẫn đến thư mục bạn muốn quét
directory_path = "./"

# Lấy danh sách tất cả các file .py trong thư mục
py_files = [f for f in os.listdir(directory_path) if f.endswith(".py")]

print("Các file .py trong thư mục:")
for file in py_files:
    print(file)
    # Đọc nội dung file
    with open(directory_path + "/" + file, "r", encoding="utf-8") as f:
        content = f.read()

    
    # content = content.replace("from library.utils import setup_logging", "")

    # content = content.replace("from .utils import setup_logging", "")

    # content = content.replace("setup_logging()", "")
    # content = content.replace("import logging", "")
    # content = content.replace("logger = logging.getLogger(__name__)", "")
    # content = content.replace("import setup_logging,", "import ")
    # content = content.replace("setup_logging(args, reset=True)", "")

    # content = content.replace("add_logging_arguments(parser),", "")
    # content = content.replace("add_logging_arguments,", "")

    # content = content.replace("logger.info(", "print(")
    # content = content.replace("logger.warning(", "print(")
    # content = content.replace("logger.error(", "print(")
    # # print(content)
    content = content.replace(", add_logging_arguments", "")
    content = content.replace("add_logging_arguments(parser)", "")
    
    # break

    # # Ghi nội dung đã thay thế vào lại file (hoặc tạo file mới)
    with open(directory_path + "/" + file, "w", encoding="utf-8") as fp:
        fp.write(content)

    print("Đã thay thế nội dung thành công!")

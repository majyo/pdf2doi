import os
import re
import shutil

from PyPDF2 import PdfFileReader



# def get_safe_filename(directory, base_name, extension):
#     """生成安全的文件名并处理冲突"""
#     counter = 1
#     clean_base = sanitize_filename(base_name)
#     filename = f"{clean_base}{extension}"
#     new_path = os.path.join(directory, filename)
#
#     # 处理文件名冲突
#     while os.path.exists(new_path):
#         filename = f"{clean_base}_{counter}{extension}"
#         new_path = os.path.join(directory, filename)
#         counter += 1
#
#     return new_path, filename
#
# def sanitize_filename(doi):
#     """清理DOI字符串中的非法文件名字符"""
#     # 移除DOI前缀（如果存在）
#     doi = re.sub(r'^doi:', '', doi, flags=re.IGNORECASE)
#
#     # 替换非法字符为下划线
#     illegal_chars = r'[\\/*?:"<>|]'
#     sanitized = re.sub(illegal_chars, '_', doi)
#
#     # 删除控制字符和不可打印字符
#     sanitized = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', sanitized)
#
#     # 移除首尾空白和点号（Windows文件名限制）
#     sanitized = sanitized.strip().strip('.')
#
#     # 确保文件名长度合理
#     max_length = 200  # 保守的文件名长度限制
#     return sanitized[:max_length]
#
# SOURCE_DIR = '../examples/false_positive/'
#
# def main():
#     # 创建目标文件夹
#     output_dir = "renamed_pdfs"
#     os.makedirs(output_dir, exist_ok=True)
#
#     # 统计处理结果
#     success_count = 0
#     fail_count = 0
#     # pdf2doi.config.set('verbose', False)
#     pdf2doi.config.set('websearch', False)
#     # 获取当前目录下所有PDF文件
#     for filename in os.listdir(SOURCE_DIR):
#         if not filename.lower().endswith('.pdf'):
#             continue
#
#         # filepath = os.path.abspath(filename)
#         filepath = os.path.join(SOURCE_DIR, filename)
#         print(f"\nProcessing: {filename}")
#
#         try:
#             # 尝试提取DOI
#             result = pdf2doi.pdf2doi(filepath)
#
#             if result and 'identifier' in result and result['identifier']:
#                 doi = result['identifier']
#                 print(f"  Found DOI: {doi}")
#
#                 # 清理DOI用于文件名
#                 clean_doi = sanitize_filename(doi)
#                 new_filename = f"{clean_doi}.pdf"
#                 new_path = os.path.join(output_dir, new_filename)
#
#                 # 处理文件名冲突
#                 counter = 1
#                 while os.path.exists(new_path):
#                     base, ext = os.path.splitext(new_filename)
#                     new_filename = f"{base}_{counter}{ext}"
#                     new_path = os.path.join(output_dir, new_filename)
#                     counter += 1
#
#                 # 复制文件到新位置
#                 shutil.copy2(filepath, new_path)
#                 print(f"  Renamed to: {new_filename}")
#                 success_count += 1
#             else:
#                 # 分离文件名和扩展名
#                 base_name, extension = os.path.splitext(filename)
#
#                 # 生成安全文件名
#                 new_path, new_filename = get_safe_filename(
#                     output_dir, base_name, extension
#                 )
#
#                 # 复制文件
#                 shutil.copy2(filepath, new_path)
#                 print(f"  Copied as: {new_filename}")
#                 print("  DOI not found")
#                 fail_count += 1
#
#         except Exception as e:
#             print(f"  Error processing file: {str(e)}")
#             fail_count += 1
#
#     # 打印摘要报告
#     print("\n" + "=" * 50)
#     print(f"Processing complete!\nSuccess: {success_count}\nFailed: {fail_count}")
#     print(f"Renamed PDFs saved to: {os.path.abspath(output_dir)}")
#     print("=" * 50)


def run_pdf_metadata_sample(file_name: str) -> None:
    pdf = PdfFileReader(file_name, strict=False)
    info = pdf.getDocumentInfo()
    for key, value in info.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    sample_filename_1 = "..\\examples\\false_positive\\unknown_article.pdf"
    sample_filename_2 = "..\\examples\\2404.16130v2.pdf"
    run_pdf_metadata_sample(sample_filename_1)

import sys
import markdown
import os

def main():
    if len(sys.argv) < 4:
        print("エラー：引数が正しくありません。" \
        "使い方：python3 file_converter.py markdown inputfile outpotfile")
        return
    if sys.argv[1] == "markdown":
        inputfile = sys.argv[2]
        outputfile = sys.argv[3]
        inputtype = os.path.splitext(inputfile)[1]
        outputtype = os.path.splitext(outputfile)[1]
        if inputtype != '.md':
            print("エラー：マークダウンファイルを指定してください。")
            return
        if outputtype != '.html':
            print("エラー：出力先にはHTMLファイルを指定してください。")
            return
        with open(inputfile,'r',encoding='utf-8') as f:
            contents = f.read()
            html = markdown.markdown(contents,extensions=["tables"])
        with open(outputfile,'w',encoding='utf-8') as f:
            f.write(html)
            return
    else:
        print("エラー：無効な操作です。")
        return
    
if __name__ == "__main__":
    main()

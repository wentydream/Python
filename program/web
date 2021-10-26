# ------------------------------------
# json.loads() 装载
# json.dumps() 卸载 返回类型为Content-Type:text/html
# jsonify()返回类型为Content-Type: application/json

# 换行符 os.linesep \r\n
# 分隔符 os.altsep /
# ------------------------------------
# 导入Flask类
from flask import Flask,render_template,request,jsonify,send_from_directory
import os


# 实例化，可视为固定格式
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False # 1.解决中文
# 获取当前运行目录下static路径，可直接浏览器访问
file_dir = f'{os.path.abspath(os.path.dirname(__file__))}'
# route()方法用于设定路由；类似spring路由配置
@app.route('/')
def login():
    return  render_template('file.html',filepath = scanfile())

# 上传文件
@app.route('/upload',methods=['POST'],strict_slashes=False)
def api_upload():
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)   # 自动创建所有目录
    
    for f in request.files.getlist('myfile'):  # 从表单的file字段获取文件，myfile为该表单的name值
        f.save(os.path.join(file_dir,f.filename))  #保存文件到file_dir目录

    # return jsonify({"resno":0,"msg":"上传成功"})    
    # return json.dumps({"resno":0,"msg":"上传成功"},ensure_ascii=False)# 2.解决中文

# 下载文件 
@app.route('/download/<path:filename>')
def download(filename):
    return send_from_directory(file_dir,filename, as_attachment=True)
# 扫描文件
def scanfile():
    filepath = [];
    for (dir_path, dir_names, file_names) in os.walk(file_dir):
        # for dir_name in dir_names: #只获取文件夹
        #     filepath.append(dir_name)
        relative_path = dir_path.replace(file_dir,"").replace("\\","") #替换掉绝对路径
        relative_path = relative_path if relative_path=="" else f'{relative_path}/'#补充缺失的/
        for file_name in file_names: #只获取文件
            filepath.append(f'{relative_path}{file_name}') #拼接文件路径
    return filepath

if __name__ == '__main__':
    # app.run(host, port, debug, options)
    # 默认值：host="127.0.0.1", port=5000, debug=False    
    app.run(host="0.0.0.0", port=5000)

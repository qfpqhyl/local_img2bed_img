# local_img2bed_img
将⌈markdown⌋中的本地图片一键上传到图床并替换⌈markdown⌋中的路径引用。

## 功能

这个项目包含以下功能：

1. **获取文件编码**：`get_encoding(file_path)`函数用于获取指定文件的编码。

2. **上传图片**：`upload_image(image_path)`函数用于将图片上传到图床，并返回图片的URL。

3. **替换链接**：`replace_image_links_in_file(file_path, new_file_path)`函数用于替换⌈markdown⌋中的文件链接。

   ------

   图床上传功能是通过抓包[Telegraph-Image](https://github.com/cf-pages/Telegraph-Image)项目得到的。

## 安装依赖

使用以下命令安装项目依赖：

```bash
pip install requests
pip install chardet
```

## 如何使用

这个Python脚本的主要功能是将Markdown文件中的本地图片链接替换为图床上的链接。以下是如何使用这个脚本的步骤：

1. 打开终端或命令行窗口。

2. 导航到包含此脚本的目录。

3. 运行以下命令：

```bash
python local2bed.py [file_path] --output [output_directory]
```

其中：

- `[file_path]` 是你想要处理的Markdown文件的路径。如果你不提供这个参数，脚本将默认处理当前目录下的所有Markdown文件（`*.md`）。

- `[output_directory]` 是处理后的文件的输出目录。如果你不提供这个参数，脚本将默认将文件输出到名为`Output`的目录。

例如，如果你想要处理名为`example.md`的文件，并将处理后的文件输出到名为`Processed`的目录，你可以运行以下命令：

```bash
python local2bed.py example.md --output Processed
```

如果你想要处理当前目录下的所有Markdown文件，并将处理后的文件输出到默认的`Output`目录，你可以运行以下命令：

```bash
python local2bed.py
```

此外，你还可以通过release下载打包好的⌈exe⌋文件运行，将上述命令中的`python local2bed.py`统一替换为`local2bed.exe`即可。



> MIT License
>
> Copyright (c) 2023 秋风飘起黄叶落

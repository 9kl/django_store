# django_store

django 基于[minio](https:://www.minio.io 'minio官方文档')的文件存储存储服务

## 安装
    pip install django_fstore

## MinioStore对象说明

- put_file 文件上传
- put_chunk_object 文件分块上传
- put_object 对象上传
- get_object 获取对象
- get_presigned_object 获取预签名的对象url

## 配置

### django setting.py 配置
    MINIO_ENDPOINT = '127.0.0.1:9000'
    MINIO_ACCESS_KEY = 'abc'
    MINIO_SECRET_KEY = 'cba'
    MINIO_SECURE = False
    MINIO_BUCKET_NAME = '2017'

### django urls.py 配置
    from django_store.views import MinioDownloadView, MinioOpenView, MinioSignedView
    
    urlpatterns = patterns(
        '',
        url(r'^minio/download/$', MinioDownloadView.as_view(), name='minio_download'),
        url(r'^minio/open/$', MinioOpenView.as_view(), name='minio_open'),
        url(r'^minio/signed/$', MinioSignedView.as_view(), name='minio_signed'),
    )
    
## 示例

### 文件上传
    from django_store.store import MinioStore
    
    def test(self, request):
        uf = request.FILES['plan_url_file']
        file_save_name = 'abc.pdf'

        ms = MinioStore()
        ms.put_file(uf, file_save_name)
        
### 文件打开
    <a href="http://127.0.0.1:8000/minio/open/?file=abc.pdf">下载</a>
    
- 下载文件
http://127.0.0.1:8000/minio/download/?file=abc.pdf
- 浏览器中打开文件
http://127.0.0.1:8000/minio/open/?file=abc.pdf
- 重定向到预签名的对象url(用于分享，可设置链接的过期时间)
http://127.0.0.1:8000/minio/signed/?file=abc.pdf

## 刷机



系统镜像： https://developer.download.nvidia.cn/embedded/L4T/r32_Release_v4.2/nv-jetson-nano-sd-card-image-r32.4.2.zip?PxiRJAAGijeFtcFPrs41xBwCHvjHwCSRc9nJQNnubdi5F_qDm5ACcELMPLAeQVmFmGLFx3E_9GqcEcS52Y7k4C669YW7XMYpHPtqPBsndvsdVXbTpM-CYPCbSeIxnvhPmvQ6JyLNy8ZcheOEtHxXvPqbwx1d0rqIs3Qmwq1VNBWlYEbfDA

## 环境配置

1，安装工具

```bash
sudo apt-get install python3-pip
sudo -H pip3 install -U jetson-stats #查看系统状态工具
sudo apt-cache show nvidia-jetpack #查看jetpack版本
```



安装scipy

```bash
sudo apt-get install liblapack-dev
sudo apt-get install libblas-dev
sudo apt-get install gfortran
pip3 install scipy
```




# you can drop this if it's already done
sudo apt-get update

# this installs git, OpenCV + python, pip
sudo apt-get install git -y
git clone https://github.com/jayrambhia/Install-OpenCV
cd Install-OpenCV/Ubuntu
./opencv_latest.sh
sudo apt-get install python-pip ipython -y

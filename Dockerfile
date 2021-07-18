# We're using Ubuntu 20.10
FROM vckyouuu/geezprojects:buster

#
# Clone repo and prepare working directory
#
RUN git clone -b alpha https://github.com/vckyou/Geez /home/geez/
RUN mkdir /home/geez/bin/
WORKDIR /home/geez/

# Upgrade pip
RUN pip install --upgrade pip

#Install python requirements
# RUN pip3 install -r https://raw.githubusercontent.com/vckyou/Geez/alpha/requirements.txt

CMD ["python3","-m","userbot"]

# -*- coding: gbk -*-
import sys
import telnetlib
import time;

HOST = "127.0.0.1"
USER = b"administrator"
PASS = b""
cmd = b"ipconfig"  # �˴�Ҳ����Ϊipconfig
tn = telnetlib.Telnet(HOST)
tn.set_debuglevel(0);
print("���ڼ����ļ������Եȡ���");
# ����5�룬��Ȼ�ڶ��ζ�ȡҲ���ܶ�������
time.sleep(5)
# ��ƥ�䵽loginʱ�����ѳɹ����ӵ�HOST���������Ϊ�����ʺ���ʾ
tn.read_until(b"login:")
# ���������͵�½�ʺţ�ģ���������
tn.write(USER + b"rn")
# print("login success");
# ���������͵�½���룬ģ���������
tn.read_until(b"password:")
tn.write(PASS + b"rn")
# print("password success");
# �ж��Ƿ�ɹ���½����
tn.read_until(b"Microsoft Telnet Server")
# ������������Ӧ��DOS������
tn.write(cmd + b"rn")
# print("cmd success");
tn.write(b"exitrn")
# ��ȡ��ƥ�䵽������
ra = tn.read_all()
# print(type(ra));
print(ra.decode('gbk'));
tn.close()
print("��ȡ��������");
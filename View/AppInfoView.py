#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter
import PIL.Image
import PIL.ImageTk

from Lib import Tools
from Da import AppBase

class GUI :

	def __init__ (self) :
		self.winTitle = 'Information'
		self.Tools = Tools.Tools()
		self.app = AppBase.info

	def show (self) :
		self.slave = Tkinter.Toplevel()
		self.slave.title(self.winTitle)
		self.slave.resizable(width = 'false', height = 'false')
		if self.Tools.isWin() :
			self.slave.iconbitmap(self.Tools.getRes('biticon.ico'))

		info = [
			'简介: 就是瞎做来看电影的。',
			'功能: 自动搜索电影资源，获取下载链接，发送至百度云，实现在线观看/离线下载功能。',
			'使用方法: 输入电影名称关键字，搜索电影。双击选中对应资源，再详细列表中的格式，可选择离线下载/在线观看/获取链接。',
			'在线观看: 资源将传输至百度云，软件将自动调用网页版播放器，也可以使用平板设备在官方app中观看。',			
			'离线下载: 资源将传输至百度云，软件将自动获取破解后的网盘下载链接，并调用本地Aria2进行下载。',		
			'附注1: 磁力链接由于包含不止一个文件，暂不支持离线下载&在线观看。',
			'附注2: 所用功能需要使用云服务，如资源较新，云服务未能识别，将不能使用离线下载&在线观看。',
			'附注3: 使用多种私密tricks，随时可能不好使。'
		]

		titleFrame = Tkinter.Frame(self.slave, bd = 0, bg="#444")
		titleFrame.pack(expand = True, fill = 'both', ipadx = '5')

		titleLabel = Tkinter.Label(titleFrame, text="Movie Catcher", fg = '#ddd', bg="#444", font = ("Helvetica", "16", 'bold'), anchor = 'center')
		titleLabel.grid(row = 0, column = 1, pady = 5)

		warnlabel = Tkinter.Label(titleFrame, text="By ~EvilCult", fg = '#ddd', bg="#444", font = ("Helvetica", "10"), anchor = 'center')
		warnlabel.grid(row = 1, column = 1)

		pilImage = PIL.Image.open(self.Tools.getRes('logo.png'))
		logoImg = PIL.ImageTk.PhotoImage(pilImage)

		imglabel = Tkinter.Label(titleFrame, bd = 0, bg = '#444', image = logoImg, anchor = 'center')
		imglabel.img = logoImg
		imglabel.grid(row = 2, column = 1, pady = 5)

		information = Tkinter.Text(titleFrame, height = 14, width = 35, bd = 0, fg = '#ddd', bg="#222", highlightthickness = 1, highlightcolor="#111", highlightbackground = '#111', selectbackground = '#116cd6', font = ("Helvetica", "12"))
		information.grid(row = 3, column = 1)
		for n in info :
			information.insert('end', n.split(': ')[0] + ':\n')
			information.insert('end', n.split(': ')[1] + '\r')

		versionlabel = Tkinter.Label(titleFrame, text="Version: " + str(self.app['ver']) + ' (' + str(self.app['build']) + ')', fg = '#ddd', bg="#444", font = ("Helvetica", "10"), anchor = 'center')
		versionlabel.grid(row = 4, column = 1)

		titleFrame.grid_columnconfigure(0, weight=1)
		titleFrame.grid_columnconfigure(2, weight=1)
# -*- coding: utf-8 -*-
from odoo import models, fields, api
from selenium import webdriver
import time
import glob
import os, sys
import base64
import pandas as pd
import csv
import xlrd
from xlsxwriter.workbook import Workbook


class SeleniumAutomate(models.TransientModel):
	_name = 'selenium.automate'
	# xls_file_info_company = fields.Binary("Importation des infos de l'entreprise")
	#Specification dernier fichier Excel à importer dans Odoo
	

	def submit_url_to_convert(self):
		
		# specifies the path to the chromedriver.exe
		driver = webdriver.Chrome()

		# driver.get method() will navigate to a page given by the URL address
		driver.get('https://convertio.co/fr/csv-xlsx/')
		time.sleep(1)

		button_url = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[1]/div[1]/div/div/span[3]')

		button_url.click()
		time.sleep(1)

		input_url = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div/div/input')
		time.sleep(1)

		input_url.send_keys('https://cache1.phantombooster.com/njdeZtkJiJo/em9HY10w25rWJsYFO13BCw/result.csv')

		button_submit_url = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/p[2]/button')
		time.sleep(1)

		button_submit_url.click()
		time.sleep(1)

		button_convert = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/button')

		button_convert.click()
		time.sleep(8)

		button_download = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[1]/table/tbody/tr/td[6]/a')

		button_download.click()
		time.sleep(1)

		path_to_directory = min(glob.iglob('/home/dev/Téléchargements/*.xlsx'), key=os.path.getctime)
		print "&"*50
		print path_to_directory

		infoc = xlrd.open_workbook(path_to_directory)
		for sheet in infoc.sheets():
			for row in range(sheet.nrows):
				array = []
				for col in range(sheet.ncols):
					array.append(sheet.cell(row,col).value)  
					if array:
						leads = self.env['crm.lead'].search([('name','ilike',array[0].encode('utf-8'))])
	                if leads:
	                	leads.update({'contact_description':array[2], 'contact_website':array[4], 'contact_secteur':array[7], 'contact_employee_quantity':array[8], 'city':array[9], 'contact_type_company':array[10], 
	                		'contact_linkedin':array[26], 'street':array[37]})

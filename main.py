# Coding UTF-8
from http.client import OK
from unittest.mock import DEFAULT
from xmlrpc.client import DateTime
import PySimpleGUI as sg
import os
from tabnanny import check
from tracemalloc import start
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
import configparser
import datetime
from addschedules import add_schedules

# Import user func
from verify_format import *
from generate_datetime import *
from datetime_master import *
from check_token import check_token_expiration
import windowlayout

# tiken.pickleが作成から一週間経過したら削除
check_token_expiration()

# If modifying these scopes, delete the file token.pickle.
# 設定ファイルの読み込み
config = configparser.ConfigParser()
config.read('./setting/setting.ini')
SCOPES = []
SCOPES.append(config['DEFAULT']['scope'])

# SCOPES = '[' + config['DEFAULT']['scope'] + ']'


def main():
    # GUIWindowを出力
    window = sg.Window('GoogleCalendarに予定を追加',
                       windowlayout.windowlayout, resizable=True)
    # イベント待機状態へ移行
    while True:
        event, values = window.read()
        # windowが閉じられたり、キャンセルボタンが押されたときプログラムを終了
        if event == sg.WIN_CLOSED or event == 'Cancell':
            break
        # 登録ボタンが押された時の処理
        if event == 'Submit':
            add_schedules(values)
    window.close()


if __name__ == '__main__':
    main()

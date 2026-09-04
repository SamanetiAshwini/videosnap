from django.http import HttpRequest, HttpResponse
from products.models import ChatHistory
from django.shortcuts import render
from django.contrib import messages
import os
import requests

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key="
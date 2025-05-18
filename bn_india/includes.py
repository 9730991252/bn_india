from django.shortcuts import render, redirect, get_object_or_404
from home.models import *
from sunil.models import *
from office.models import *
from django.contrib import messages
import time
import io
import os
import base64
import math
from datetime import date
from datetime import datetime
from django.db.models import *
from django.template.loader import render_to_string
from django.db.models import Avg, Sum, Min, Max
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.files.base import ContentFile
from django.utils.timezone import localtime
import json
from django.http import StreamingHttpResponse
from django.utils.timezone import now
from django.core.paginator import Paginator
from django.db.models import F
from django.db import models
from django.contrib.sessions.models import Session
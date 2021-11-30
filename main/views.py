from django.shortcuts import render
from rest_framework import serializers, status, generics
from rest_framework.response import Response
import cv2
import numpy as np
from .models import MaskCategory
from django.conf import settings

# Create your views here.
class MainApi(generics.GenericAPIView):


    def post(self, request, format=None):
        mask_image = request.FILES.get('mask_image')
        for_masking = request.FILES.get('for_masking')

        mask = MaskCategory(
            mask_image=mask_image,
            for_masking=for_masking
        )
        mask.save()
        src1 = str(settings.BASE_DIR) + f"\media\mask\{str(mask_image)}"
        src2 = str(settings.BASE_DIR) + f"\media\main\{str(for_masking)}"

        path1 = cv2.imread(src1)
        path2 = cv2.imread(src2)

        # main mechanism of masking
        path2 = cv2.resize(path2, path1.shape[1::-1])

        # uint8
        dst = cv2.bitwise_and(path1, path2, path1)


        # for removing black background
        tmp = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
        _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
        b, g, r = cv2.split(dst)
        rgba = [b,g,r, alpha]
        dst = cv2.merge(rgba,4)
        cv2.imshow('showresult', dst)
        cv2.imwrite("test.png", dst)



        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return Response({'data':"response"})

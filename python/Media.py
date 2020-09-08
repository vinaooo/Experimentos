#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Media.py
#  
#  Copyright 2020 Vinicius <ubuntu@ubuntu>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

nota1 = input("Digite a nota 1: ")
nota2 = input("Digite a nota 2: ")

media = eval(nota1)*0.4 + eval(nota2)*0.6

if media >= 5:
    print("Aprovado")

else:
    print("Reprovado")

# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHRraW50ZXIKaW1wb3J0IHN1YnByb2Nlc3MKZnJvbSB0a2ludGVyIGltcG9ydCAqCmZyb20gdGtpbnRlciBpbXBvcnQgZmlsZWRpYWxvZwppbXBvcnQgdGtpbnRlciBhcyB0awpmcm9tIHRraW50ZXIgaW1wb3J0IG1lc3NhZ2Vib3gKaW1wb3J0IHRraW50ZXIuZm9udCBhcyBmb250CmZyb20gUElMIGltcG9ydCBJbWFnZVRrLCBJbWFnZQppbXBvcnQgdXJsbGliLnJlcXVlc3QKZnJvbSBpbyBpbXBvcnQgQnl0ZXNJTwppbXBvcnQgb3MKaW1wb3J0IGlvCmltcG9ydCBzeXMKaW1wb3J0IHBpY2tsZQppbXBvcnQgdGltZQpmcm9tIGRlY2ltYWwgaW1wb3J0ICoKaW1wb3J0IHdlYmJyb3dzZXIKZnJvbSBzZWxlbml1bSBpbXBvcnQgd2ViZHJpdmVyCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNvbW1vbi5ieSBpbXBvcnQgQnkKZnJvbSBzZWxlbml1bS53ZWJkcml2ZXIuc3VwcG9ydC53YWl0IGltcG9ydCBXZWJEcml2ZXJXYWl0CmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNocm9tZS5vcHRpb25zIGltcG9ydCBPcHRpb25zCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLnN1cHBvcnQgaW1wb3J0IGV4cGVjdGVkX2NvbmRpdGlvbnMgYXMgRXhwZWN0ZWRDb25kaXRpb25zCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNvbW1vbi5rZXlzIGltcG9ydCBLZXlzCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLnN1cHBvcnQudWkgaW1wb3J0IFNlbGVjdAppbXBvcnQganNvbiAKaW1wb3J0IHNzbAppbXBvcnQgY2VydGlmaQoKcm9vdCA9IFRrKCkKCnJvb3QuZ2VvbWV0cnkoJzc1MHg3NTAnKQpyb290LnJlc2l6YWJsZShGYWxzZSwgRmFsc2UpCnJvb3QudGl0bGUoIk5GVHMgVXBsb2FkIHRvIE9wZW5TZWEgdjEuMCIpCiAgCmlucHV0X3NhdmVfbGlzdCA9IFsiTkZUcyBmb2xkZXIgOiIsIDAsIDAsIDAsIDAsIDAsIDAsIDAsIDBdCm1haW5fZGlyZWN0b3J5ID0gb3MucGF0aC5qb2luKHN5cy5wYXRoWzBdKQoKCmRlZiBzdXBwb3J0VVJMKCk6CiAgICB3ZWJicm93c2VyLm9wZW5fbmV3KCJodHRwczovL3d3dy5pbmZvdHJleC5uZXQvb3BlbnNlYS9zdXBwb3J0LmFzcD9yPWFwcCIpCgpkZWYgY29mZmVlVVJMKCk6CiAgICB3ZWJicm93c2VyLm9wZW5fbmV3KCJodHRwczovL2dpdGh1Yi5jb20vaW5mb3RyZXgvYnVsay11cGxvYWQtdG8tb3BlbnNlYS8jdGhhbmtzIikKCmNsYXNzIFdlYkltYWdlOgogICAgZGVmIF9faW5pdF9fKHNlbGYsIHVybCk6CiAgICAgICAgd2l0aCB1cmxsaWIucmVxdWVzdC51cmxvcGVuKHVybCkgYXMgdToKICAgICAgICAgICAgcmF3X2RhdGEgPSB1LnJlYWQoKQogICAgICAgICNzZWxmLmltYWdlID0gdGsuUGhvdG9JbWFnZShkYXRhPWJhc2U2NC5lbmNvZGVieXRlcyhyYXdfZGF0YSkpCiAgICAgICAgaW1hZ2UgPSBJbWFnZS5vcGVuKGlvLkJ5dGVzSU8ocmF3X2RhdGEpKQogICAgICAgIHNlbGYuaW1hZ2UgPSBJbWFnZVRrLlBob3RvSW1hZ2UoaW1hZ2UpCgogICAgZGVmIGdldChzZWxmKToKICAgICAgICByZXR1cm4gc2VsZi5pbWFnZQppbWFnZXVybCA9ICJodHRwczovL3d3dy5pbmZvdHJleC5uZXQvb3BlbnNlYS9oZWFkZXIucG5nIgppbWcgPSBXZWJJbWFnZShpbWFnZXVybCkuZ2V0KCkKaW1hZ2VsYWIgPSB0ay5MYWJlbChyb290LCBpbWFnZT1pbWcpCmltYWdlbGFiLmdyaWQocm93PTAsIGNvbHVtbnNwYW49MikKaW1hZ2VsYWIuYmluZCgiPEJ1dHRvbi0xPiIsIGxhbWJkYSBlOnN1cHBvcnRVUkwoKSkKCmlzX3BvbHlnb24gPSBCb29sZWFuVmFyKCkKaXNfcG9seWdvbi5zZXQoVHJ1ZSkKCmlzX2xpc3RpbmcgPSBCb29sZWFuVmFyKCkKaXNfbGlzdGluZy5zZXQoVHJ1ZSkgCgppc19udW1mb3JtYXQgPSBCb29sZWFuVmFyKCkKaXNfbnVtZm9ybWF0LnNldChGYWxzZSkgCgoKCgpkZWYgb3Blbl9jaHJvbWVfcHJvZmlsZSgpOgogICAgc3VicHJvY2Vzcy5Qb3BlbigKICAgICAgICBbCiAgICAgICAgICAgICJzdGFydCIsCiAgICAgICAgICAgICJjaHJvbWUiLAogICAgICAgICAgICAiLS1yZW1vdGUtZGVidWdnaW5nLXBvcnQ9ODk4OSIsCiAgICAgICAgICAgICItLXVzZXItZGF0YS1kaXI9IiArIG1haW5fZGlyZWN0b3J5ICsgIi9jaHJvbWVfcHJvZmlsZSIsCiAgICAgICAgXSwKICAgICAgICBzaGVsbD1UcnVlLAogICAgKQoKCmRlZiBzYXZlX2ZpbGVfcGF0aCgpOgogICAgI3JldHVybiBvcy5wYXRoLmpvaW4oc3lzLnBhdGhbMF0sICJTYXZlX2ZpbGUuY2xvdWQiKSAKICAgIHJldHVybiBvcy5wYXRoLmpvaW4oc3lzLnBhdGhbMF0sICJTYXZlX2d1aS5jbG91ZCIpIAoKCiMgYXNrIGZvciBkaXJlY3Rvcnkgb24gY2xpY2tpbmcgYnV0dG9uLCBjaGFuZ2VzIGJ1dHRvbiBuYW1lLgpkZWYgdXBsb2FkX2ZvbGRlcl9pbnB1dCgpOgogICAgZ2xvYmFsIHVwbG9hZF9wYXRoCiAgICB1cGxvYWRfcGF0aCA9IGZpbGVkaWFsb2cuYXNrZGlyZWN0b3J5KCkKICAgIE5hbWVfY2hhbmdlX2ltZ19mb2xkZXJfYnV0dG9uKHVwbG9hZF9wYXRoKQoKZGVmIE5hbWVfY2hhbmdlX2ltZ19mb2xkZXJfYnV0dG9uKHVwbG9hZF9mb2xkZXJfaW5wdXQpOgogICAgdXBsb2FkX2ZvbGRlcl9pbnB1dF9idXR0b25bInRleHQiXSA9IHVwbG9hZF9mb2xkZXJfaW5wdXQKCmRlZiBpc19udW1lcmljKHZhbCk6CglpZiBzdHIodmFsKS5pc2RpZ2l0KCk6CgkJcmV0dXJuIFRydWUKCWVsaWYgc3RyKHZhbCkucmVwbGFjZSgnLicsJycsMSkuaXNkaWdpdCgpOgoJCXJldHVybiBUcnVlCgllbHNlOgoJCXJldHVybiBGYWxzZQoKY2xhc3MgSW5wdXRGaWVsZDoKICAgIGRlZiBfX2luaXRfXyhzZWxmLCBsYWJlbCwgcm93X2lvLCBjb2x1bW5faW8sIHBvcywgIG1hc3Rlcj1yb290KToKICAgICAgICBzZWxmLm1hc3RlciA9IG1hc3RlcgogICAgICAgIHNlbGYuaW5wdXRfZmllbGQgPSBFbnRyeShzZWxmLm1hc3Rlciwgd2lkdGg9NjApCiAgICAgICAgc2VsZi5pbnB1dF9maWVsZC5ncmlkKGlwYWR5PTMpCiAgICAgICAgc2VsZi5pbnB1dF9maWVsZC5sYWJlbCA9IExhYmVsKG1hc3RlciwgdGV4dD1sYWJlbCwgYW5jaG9yPSJ3Iiwgd2lkdGg9MjAsIGhlaWdodD0xICkKICAgICAgICBzZWxmLmlucHV0X2ZpZWxkLmxhYmVsLmdyaWQocm93PXJvd19pbywgY29sdW1uPWNvbHVtbl9pbywgcGFkeD0xMiwgcGFkeT0yKQogICAgICAgIHNlbGYuaW5wdXRfZmllbGQuZ3JpZChyb3c9cm93X2lvLCBjb2x1bW49Y29sdW1uX2lvICsgMSwgcGFkeD0xMiwgcGFkeT0yKQogICAgICAgIHRyeToKICAgICAgICAgICAgd2l0aCBvcGVuKHNhdmVfZmlsZV9wYXRoKCksICJyYiIpIGFzIGluZmlsZToKICAgICAgICAgICAgICAgIG5ld19kaWN0ID0gcGlja2xlLmxvYWQoaW5maWxlKQogICAgICAgICAgICAgICAgc2VsZi5pbnNlcnRfdGV4dChuZXdfZGljdFtwb3NdKQogICAgICAgIGV4Y2VwdCBGaWxlTm90Rm91bmRFcnJvcjoKICAgICAgICAgICAgcGFzcwogICAgICAgIAogICAgZGVmIGluc2VydF90ZXh0KHNlbGYsIHRleHQpOgogICAgICAgIHNlbGYuaW5wdXRfZmllbGQuZGVsZXRlKDAsICJlbmQiKQogICAgICAgIHNlbGYuaW5wdXRfZmllbGQuaW5zZXJ0KDAsIHRleHQpCgogICAgZGVmIHNhdmVfaW5wdXRzKHNlbGYsIHBvcyk6CiAgICAgICAgI21lc3NhZ2Vib3guc2hvd3dhcm5pbmcoInNob3d3YXJuaW5nIiwgIldhcm5pbmciKQogICAgICAgIGlucHV0X3NhdmVfbGlzdC5pbnNlcnQocG9zLCBzZWxmLmlucHV0X2ZpZWxkLmdldCgpKQogICAgICAgIHdpdGggb3BlbihzYXZlX2ZpbGVfcGF0aCgpLCAid2IiKSBhcyBvdXRmaWxlOgogICAgICAgICAgICBwaWNrbGUuZHVtcChpbnB1dF9zYXZlX2xpc3QsIG91dGZpbGUpCiAgICAgICAgICAgIAogICAgZGVmIHZhbGlkYXRlX2lucHV0cyhzZWxmLCBtYXhsZW4sIHR5cGUsIG1lc3NhZ2UpOgoKICAgICAgICBpZiB0eXBlID09IDAgYW5kIChsZW4oc2VsZi5pbnB1dF9maWVsZC5nZXQoKSkgPT0gMCBvciAoc2VsZi5pbnB1dF9maWVsZC5nZXQoKSkuaXNkaWdpdCgpICE9IFRydWUgb3IgbGVuKHNlbGYuaW5wdXRfZmllbGQuZ2V0KCkpID4gbWF4bGVuKToKICAgICAgICAgICAgbWVzc2FnZWJveC5zaG93d2FybmluZygic2hvd3dhcm5pbmciLCBtZXNzYWdlKQogICAgICAgICAgICAg'
love = 'VPNtPvNtVPNtVPNtMJkcMvO0rKOyVQ09VQRtLJ5xVPufMJ4bp2IfMv5coaO1qS9znJIfMP5aMKDbXFxtCG0tZPOipvOcp19hqJ1ypzywXUAyoTLhnJ5jqKEsMzyyoTDhM2I0XPxcVQ09VRMuoUAyVT9lVTkyovumMJkzYzyhpUI0K2McMJkxYzqyqPtcXFN+CFOgLKufMJ4cBtbtVPNtVPNtVPNtVPOgMKAmLJqyLz94YaAbo3q3LKWhnJ5aXPWmnT93q2SlozyhMlVfVT1yp3AuM2HcVPNtVPNtVNbtVPNtVPNtVPNtVPNtVPNtPvNtVPNtVPNtMJkcMvO0rKOyVQ09VQVtLJ5xVPttoTIhXUAyoTLhnJ5jqKEsMzyyoTDhM2I0XPxcVQ09VQNto3VtoTIhXUAyoTLhnJ5jqKEsMzyyoTDhM2I0XPxcVQ4toJS4oTIhXGbXVPNtVPNtVPNtVPNtoJImp2SaMJWirP5mnT93q2SlozyhMltvp2uiq3qupz5cozpvYPOgMKAmLJqyXDbtVPNtVPNtVPNtVPNtVPNXVPNtVPNtVPOyoUAyBtbtVPNtVPNtVPNtVPOlMKE1pz4tIUW1MFNtVPNtPvNtVPNtVPNtPtbwVlAcoaO1qPOiLzcyL3EmVlZwPzAioTkyL3Eco25soTyhn19coaO1qPN9VRyhpUI0EzyyoTDbVx9jMJ5GMJRtD29foTIwqTyiovOZnJ5eBvVfVQVfVQNfVQRcPaA0LKW0K251oI9coaO1qPN9VRyhpUI0EzyyoTDbVyA0LKW0VR51oJWypwbvYPNmYPNjYPNlXDcyozEsoaIgK2yhpUI0VQ0tFJ5jqKETnJIfMPtvEJ5xVR51oJWypwbvYPN0YPNjYPNmXDcjpzywMFN9VRyhpUI0EzyyoTDbVxEyMzS1oUDtHUWcL2H6VvjtAFjtZPjtAPxXqTy0oTHtCFOWoaO1qRMcMJkxXPWHnKEfMGbvYPN2YPNjYPN1XDcxMKAwpzyjqTyiovN9VRyhpUI0EzyyoTDbVxEyp2AlnKO0nJ9hBvVfVQpfVQNfVQLcPzMcoTIsMz9loJS0VQ0tFJ5jqKETnJIfMPtvGxMHVRygLJqyVRMipz1uqQbvYPN4YPNjYPN3XDcyrUEypz5uoS9fnJ5eVQ0tFJ5jqKETnJIfMPtvEKu0MKWhLJjtoTyhnmbvYPN5YPNjYPN4XDbXVlZwp2S2MFOcoaO1qUZwVlZXMTIzVUAuqzHbXGbXPvNtVPOcMvOfMJ4bp3EupaEsoaIgK2yhpUI0YzyhpUI0K2McMJkxYzqyqPtcXFN9CFNjVT9lVTkyovuyozEsoaIgK2yhpUI0YzyhpUI0K2McMJkxYzqyqPtcXFN9CFNjVT9lVPucoaDbMJ5xK251oI9coaO1qP5coaO1qS9znJIfMP5aMKDbXFxtCPOcoaDbp3EupaEsoaIgK2yhpUI0YzyhpUI0K2McMJkxYzqyqPtcXFx6PvNtVPNtVPNtV21yp3AuM2Ivo3thp2uiq3qupz5cozpbVaAbo3q3LKWhnJ5aVvjtVxIhMPOhqJ1vMKVtp2uiqJkxVTqlMJS0MKVtqTuuovOmqTSlqPOhqJ1vMKVuVvxXVPNtVPNtVPNwpzI0qKWhVSElqJHXVPNtVPNtVPOjpzyhqPNbVaElqJHvXDbtVPNtMJkcMvOfMJ4bVUA0LKW0K251oI9coaO1qP5coaO1qS9znJIfMP5aMKDbXFxtCG0tZPOipvOfMJ4bMJ5xK251oI9coaO1qP5coaO1qS9znJIfMP5aMKDbXFxtCvN0VQbXVPNtVPNtVPNwoJImp2SaMJWirP5mnT93q2SlozyhMltvp2uiq3qupz5cozpvYPNvH3EupaDtYlOyozDtoaIgLzIlVUWuozqyVQNtYFN5BGx5VvxXVPNtVPNtVPNwpzI0qKWhVSElqJHXVPNtVPNtVPOjpzyhqPNbVaElqJHvXDbtVPNtMJkmMGbXVPNtVPNtVPOwo2kfMJA0nJ9hK2kcozgsnJ5jqKDhqzSfnJEuqTIsnJ5jqKEmXQVjZPjtZvjtW0AioTkyL3Eco24toTyhnlOlMKS1nKWyMPpcPvNtVPNtVPNtpUWcL2HhqzSfnJEuqTIsnJ5jqKEmXQRjZPjtZFjtW1OlnJAyVUWypKIcpzIxWlxXVPNtVPNtVPO0nKEfMF52LJkcMTS0MI9coaO1qUZbZGNjYPNlYPNaqTy0oTHtpzIkqJylMJDaXDbtVPNtVPNtVTEyp2AlnKO0nJ9hYaMuoTyxLKEyK2yhpUI0pltkZQNfVQVfVPqxMKAwpzyjqTyiovOlMKS1nKWyMPpcPvNtVPNtVPNtMzyfMI9zo3WgLKDhqzSfnJEuqTIsnJ5jqKEmXQRjZPjtZvjtW2McoTHtMz9loJS0VUWypKIcpzIxVP0tpT5aYPOdpTpfVTcjMJpaXDbtVPNtVPNtVTI4qTIlozSfK2kcozfhqzSfnJEuqTIsnJ5jqKEmXQRjZPjtZljtWlpcPvNtVPNtVPNtPtbtVPNtnJ5jqKEsp2S2MI9fnKA0Yzyhp2IlqPtjYPO1pTkiLJEspTS0nPxXVPNtVTAioTkyL3Eco25soTyhn19coaO1qP5mLKMyK2yhpUI0pltkXDbtVPNtp3EupaEsoaIgK2yhpUI0YaAuqzIsnJ5jqKEmXQVcPvNtVPOyozEsoaIgK2yhpUI0YaAuqzIsnJ5jqKEmXQZcPvNtVPOjpzywMF5mLKMyK2yhpUI0plt0XDbtVPNtqTy0oTHhp2S2MI9coaO1qUZbAFxXVPNtVTEyp2AlnKO0nJ9hYaAuqzIsnJ5jqKEmXQLcPvNtVPOznJkyK2Mipz1uqP5mLKMyK2yhpUI0plt3XDbtVPNtMKu0MKWhLJksoTyhnl5mLKMyK2yhpUI0plt4XDbtVPNXPtbwVS9sK19sGHSWGy9QG0ESK19sK18XMTIzVT1unJ5spUWiM3WuoI9fo29jXPx6PvNwVlAGIRSFIPZwVjbtVPNtnJLtoTIhXTIhMS9hqJ1snJ5jqKDhnJ5jqKEsMzyyoTDhM2I0XPxcVQ4tAPN6PvNtVPNtVPNtoJImp2SaMJWirP5mnT93q2SlozyhMltvp2uiq3qupz5cozpvYPNvH3EupaDtYlOyozDtoaIgLzIlVUWuozqyVQNtYFN5BGx5VvxXVPNtVPNtVPOmrKZhMKucqPtcPtbtVPNtpUWinzIwqS9jLKEbVQ0toJScoy9xnKWyL3EipaxXVPNtVTMcoTIspTS0nPN9VUIjoT9uMS9jLKEbPvNtVPOwo2kfMJA0nJ9hK2kcozftCFOwo2kfMJA0nJ9hK2kcozgsnJ5jqKDhnJ5jqKEsMzyyoTDhM2I0XPxXVPNtVUA0LKW0K251oFN9VTyhqPumqTSlqS9hqJ1snJ5jqKDhnJ5jqKEsMzyyoTDhM2I0XPxcPvNtVPOyozEsoaIgVQ0tnJ50XTIhMS9hqJ1snJ5jqKDhnJ5jqKEsMzyyoTDhM2I0XPxcPvNtVPOfo29jK3OlnJAyVQ0tMzkiLKDbpUWcL2HhnJ5jqKEsMzyyoTDhM2I0XPxcPvNtVPOfo29jK3EcqTkyVQ0tqTy0oTHhnJ5jqKEsMzyyoTDhM2I0XPxXVPNtVTkio3OsMzyfMI9zo3WgLKDtCFOznJkyK2Mipz1uqP5coaO1qS9znJIfMP5aMKDbXDbtVPNtoT9ipS9yrUEypz5uoS9fnJ5eVQ0tp3ElXTI4qTIlozSfK2kcozfhnJ5jqKEsMzyyoTDhM2I0XPxcPvNtVPOfo29jK2Eyp2AlnKO0nJ9hVQ0tMTImL3WcpUEco24hnJ5jqKEsMzyyoTDhM2I0XPxXPvNtVPNwV2Abpz9gMJ9jqTyioaZXVPNtVT9jqPN9VR9jqTyioaZbXDbtVPNto3O0YzSxMS9yrUOypzygMJ50LJkso3O0nJ9hXPWxMJW1M2qypxSxMUWyp3ZvYPNvoT9wLJkbo3A0Bwt5BQxvXDbtVPNtMUWcqzIlVQ0tq2IvMUWcqzIlYxAbpz9gMFtXVPNtVPNtVPOyrTIwqKEuLzkyK3OuqTt9pUWinzIwqS9jLKEbVPftVv9wnUWioJIxpzy2MKVhMKuyVvjXVPNtVPNtVPOwnUWioJIso3O0nJ9hpm1ipUDfPvNtVPNcPvNtVPO3LJy0VQ0tI2IvEUWcqzIlI2ScqPuxpzy2MKVfVQLjXDbXVPNtVPZwV3qunKDtMz9lVT1yqTuiMUZXVPNtVTEyMvO3LJy0K2Amp19mMJkyL3Eipvuwo2EyXGbXVPNtVPNtVPO3LJy0YaIhqTyfXNbtVPNtVPNtVPNtVPOSrUOyL3EyMRAiozEcqTyioaZhpUWyp2IhL2Iso2MsMJkyoJIhqS9fo2AuqTIxXPuPrF5QH1AsH0IZEHAHG1VfVTAiMTHcXDbtVPNtVPNtVPxXVPNtVPNtVPNXVPNtVTEyMvO3LJy0K2Amp19mMJkyL3EipyEyp3DbL29xMFx6PvNtVPNtVPNtq2ScqP51oaEcoPtXVPNtVPNtVPNtVPNtEKujMJA0MJEQo25xnKEco25mYzIfMJ1yoaEHo0WyD2kcL2guLzkyXPuPrF5QH1AsH0IZEHAHG1VfVTAiMTHcXDbtVPNtVPNtVPxtVPNtPtbtVPNtMTIzVUqunKEsrUOuqTtbL29xMFx6PvNtVPNtVPNtq2ScqP51oaEcoPuSrUOyL3EyMRAiozEcqTyioaZhpUWyp2IhL2Iso2MsMJkyoJIhqS9fo2AuqTIxXPuPrF5LHRSHFPjtL29xMFxcXDbXPvNtVPO3nTyfMFOyozEsoaIgVQ49VUA0LKW0K251oGbXVPNtVPNtVPOcMvOcp19hqJ1zo3WgLKDhM2I0XPx6PvNtVPNtVPNtVPNtVUA0LKW0K251oJMipz1uqPN9VTLvrlOmqTSlqS9hqJ06ZQE9VtbtVPNtVPNtVTIfp2H6PvNtVPNtVPNtVPNtVPOmqTSlqS9hqJ1zo3WgLKDtCFOzVaftp3EupaEsoaIgBwNksFVXPvNtVPNtVPNtpUWcoaDbVyA0LKW0VTAlMJS0nJ5aVR5TIPNvVPftVTkio3OsqTy0oTHtXlOmqUVbp3EupaEsoaIgMz9loJS0XFxXVPNtVPNtVPOjpzyhqPtaoaIgLzIlVPpfVPOmqTSlqS9hqJ1zo3WgLKDcPvNtVPNtVPNtMUWcqzIlYzqyqPuwo2kfMJA0nJ9hK2kcozfcPvNtVPNtVPNtPvNtVPNtVPNtPvNtVPNtVPNtq2ScqS94pTS0nPtaYl8dJ0OcMQ0voJIxnJRvKFpcPvNtVPNtVPNtnJ1uM2IIpTkiLJDtCFOxpzy2MKVhMzyhMS9yoTIgMJ50K2W5K3ujLKEbXPpiYlco'
god = 'QGlkPSJtZWRpYSJdJykKICAgICAgICBpbWFnZVBhdGggPSBvcy5wYXRoLmFic3BhdGgoZmlsZV9wYXRoICsgIlxcaW1hZ2VzXFwiICsgc3RyKHN0YXJ0X251bWZvcm1hdCkgKyAiLiIgKyBsb29wX2ZpbGVfZm9ybWF0KSAgIyBjaGFuZ2UgZm9sZGVyIGhlcmUKICAgICAgICBpbWFnZVVwbG9hZC5zZW5kX2tleXMoaW1hZ2VQYXRoKQogICAgICAgIHRpbWUuc2xlZXAoMC44KQoKICAgICAgICBuYW1lID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy8qW0BpZD0ibmFtZSJdJykKICAgICAgICBuYW1lLnNlbmRfa2V5cyhsb29wX3RpdGxlICsgc3RyKHN0YXJ0X251bWZvcm1hdCkpICAjICsxMDAwIGZvciBvdGhlciBmb2xkZXJzICNjaGFuZ2UgbmFtZSBiZWZvcmUgIiMiCiAgICAgICAgdGltZS5zbGVlcCgwLjgpCgogICAgICAgIGV4dF9saW5rID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy8qW0BpZD0iZXh0ZXJuYWxfbGluayJdJykKICAgICAgICBleHRfbGluay5zZW5kX2tleXMobG9vcF9leHRlcm5hbF9saW5rKQogICAgICAgIHRpbWUuc2xlZXAoMC44KQoKICAgICAgICBkZXNjID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy8qW0BpZD0iZGVzY3JpcHRpb24iXScpCiAgICAgICAgZGVzYy5zZW5kX2tleXMobG9vcF9kZXNjcmlwdGlvbikKICAgICAgICB0aW1lLnNsZWVwKDAuOCkKCiAgICAgICAgI2pzb25EYXRhID0gSlNPTihmaWxlX3BhdGggKyAiL2pzb24vIisgc3RyKHN0YXJ0X251bSkgKyAiLmpzb24iKS5yZWFkRnJvbUZpbGUoKQoKICAgICAgICBqc29uRmlsZSA9IGZpbGVfcGF0aCArICIvanNvbi8iKyBzdHIoc3RhcnRfbnVtZm9ybWF0KSArICIuanNvbiIKICAgICAgICBpZiBvcy5wYXRoLmlzZmlsZShqc29uRmlsZSkgYW5kIG9zLmFjY2Vzcyhqc29uRmlsZSwgb3MuUl9PSyk6CiAgICAgICAgICAgCiAgICAgICAgICAgICNwcmludChzdHIoanNvbk1ldGFEYXRhKSkKICAgICAgICAgICAgd2FpdF9jc3Nfc2VsZWN0b3IoImJ1dHRvblthcmlhLWxhYmVsPSdBZGQgcHJvcGVydGllcyddIikKICAgICAgICAgICAgcHJvcGVydGllcyA9IGRyaXZlci5maW5kX2VsZW1lbnRfYnlfY3NzX3NlbGVjdG9yKCJidXR0b25bYXJpYS1sYWJlbD0nQWRkIHByb3BlcnRpZXMnXSIpCiAgICAgICAgICAgIGRyaXZlci5leGVjdXRlX3NjcmlwdCgiYXJndW1lbnRzWzBdLmNsaWNrKCk7IiwgcHJvcGVydGllcykKICAgICAgICAgICAgdGltZS5zbGVlcCgwLjgpCgogICAgICAgICAgICAjIGpzb25EYXRhID0gSlNPTihvcy5nZXRjd2QoKSArICIvZGF0YS8iKyBzdHIoc3RhcnRfbnVtKSArICIuanNvbiIpLnJlYWRGcm9tRmlsZSgpCiAgICAgICAgICAgICMganNvbk1ldGFEYXRhID0ganNvbkRhdGFbJ2F0dHJpYnV0ZXMnXQoKICAgICAgICAgICAgICMgY2hlY2tzIGlmIGZpbGUgZXhpc3RzCiAgICAgICAgICAgIGpzb25EYXRhID0ganNvbi5sb2FkcyhvcGVuKGZpbGVfcGF0aCArICJcXGpzb25cXCIrIHN0cihzdGFydF9udW1mb3JtYXQpICsgIi5qc29uIikucmVhZCgpKQogICAgICAgICAgICBqc29uTWV0YURhdGEgPSBqc29uRGF0YVsnYXR0cmlidXRlcyddCgogICAgICAgICAgICBmb3Iga2V5IGluIGpzb25NZXRhRGF0YToKICAgICAgICAgICAgICAgIGlucHV0MSA9IGRyaXZlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoJy8vdGJvZHlbQGNsYXNzPSJBc3NldFRyYWl0c0Zvcm0tLWJvZHkiXS90cltsYXN0KCldL3RkWzFdL2Rpdi9kaXYvaW5wdXQnKQogICAgICAgICAgICAgICAgaW5wdXQyID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy90Ym9keVtAY2xhc3M9IkFzc2V0VHJhaXRzRm9ybS0tYm9keSJdL3RyW2xhc3QoKV0vdGRbMl0vZGl2L2Rpdi9pbnB1dCcpCiAgICAgICAgICAgICAgICAjcHJpbnQoc3RyKGtleVsndHJhaXRfdHlwZSddKSkKICAgICAgICAgICAgICAgICNwcmludChzdHIoa2V5Wyd2YWx1ZSddKSkKICAgICAgICAgICAgICAgIGlucHV0MS5zZW5kX2tleXMoc3RyKGtleVsndHJhaXRfdHlwZSddKSkKICAgICAgICAgICAgICAgIGlucHV0Mi5zZW5kX2tleXMoc3RyKGtleVsndmFsdWUnXSkpCiAgICAgICAgICAgICAgICAjIGRyaXZlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoJy8vYnV0dG9uW3RleHQoKT0iQWRkIG1vcmUiXScpLmNsaWNrKCkKICAgICAgICAgICAgICAgIGFkZG1vcmVfYnV0dG9uID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy9idXR0b25bdGV4dCgpPSJBZGQgbW9yZSJdJykKICAgICAgICAgICAgICAgIGRyaXZlci5leGVjdXRlX3NjcmlwdCgiYXJndW1lbnRzWzBdLmNsaWNrKCk7IiwgYWRkbW9yZV9idXR0b24pCiAgICAgICAgICAgIHRpbWUuc2xlZXAoMC45KQoKICAgICAgICAgICAgZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy9idXR0b25bdGV4dCgpPSJTYXZlIl0nKS5jbGljaygpCiAgICAgICAgICAgIHRpbWUuc2xlZXAoMC44KQoKCgogICAgICAgICMgU2VsZWN0IFBvbHlnb24gYmxvY2tjaGFpbiBpZiBhcHBsaWNhYmxlCiAgICAgICAgaWYgaXNfcG9seWdvbi5nZXQoKToKICAgICAgICAgICAgIyBibG9ja2NoYWluX2J1dHRvbiA9IGRyaXZlci5maW5kX2VsZW1lbnQoQnkuWFBBVEgsICcvLypbQGlkPSJjaGFpbiJdJykKICAgICAgICAgICAgIyBkcml2ZXIuZXhlY3V0ZV9zY3JpcHQoImFyZ3VtZW50c1swXS5jbGljaygpOyIsIGJsb2NrY2hhaW5fYnV0dG9uKQogICAgICAgICAgICAjIHRpbWUuc2xlZXAoMC44KQogICAgICAgICAgICAKICAgICAgICAgICAgIyBzZWxlY3RfcG9seWdvbiA9IGRyaXZlci5maW5kX2VsZW1lbnQoQnkuWFBBVEgsICIvaHRtbC9ib2R5L2RpdlsxXS9kaXZbMV0vbWFpbi9kaXYvZGl2L3NlY3Rpb24vZGl2WzJdL2Zvcm0vZGl2WzddL2Rpdi9kaXZbM10vZGl2L2Rpdi9kaXYvdWwvbGkvYnV0dG9uIikKICAgICAgICAgICAgIyBzZWxlY3RfcG9seWdvbi5jbGljaygpCiAgICAgICAgICAgIGJsb2NrY2hhaW5fYnV0dG9uID0gZHJpdmVyLmZpbmRfZWxlbWVudChCeS5YUEFUSCwgJy8vKltAaWQ9Il9fbmV4dCJdL2RpdlsxXS9tYWluL2Rpdi9kaXYvc2VjdGlvbi9kaXYvZm9ybS9kaXZbN10vZGl2L2RpdlsyXScpCiAgICAgICAgICAgIGJsb2NrY2hhaW5fYnV0dG9uLmNsaWNrKCkKICAgICAgICAgICAgdGltZS5zbGVlcCgwLjgpCgogICAgICAgICAgICBzZWxlY3RfcG9seWdvbiA9IGRyaXZlci5maW5kX2VsZW1lbnQoQnkuWFBBVEgsICcvaHRtbC9ib2R5L2RpdlsxXS9kaXZbMV0vbWFpbi9kaXYvZGl2L3NlY3Rpb24vZGl2WzJdL2Zvcm0vZGl2WzddL2Rpdi9kaXZbM10vZGl2L2Rpdi9kaXYvdWwvbGkvYnV0dG9uJykKICAgICAgICAgICAgc2VsZWN0X3BvbHlnb24uY2xpY2soKQogICAgICAgICAgICB0aW1lLnNsZWVwKDAuOCkKCiAgICAgICAgICAgICMgYmxvY2tjaGFpbl9idXR0b24uc2VuZF9rZXlzKEtleXMuVEFCKQogICAgICAgICAgICAjIHRpbWUuc2xlZXAoMC44KQogICAgICAgICAgICAjIGJsb2NrY2hhaW5fYnV0dG9uLnNlbmRLZXlzKEtleXMuRU5URVIpOwogICAgICAgICAgICAjIHRpbWUuc2xlZXAoMC44KQogICAgICAgICAgICAjIHBvbHlnb25fYnV0dG9uX2xvY2F0aW9uID0gJy8vc3Bhbltub3JtYWxpemUtc3BhY2UoKSA9ICJNdW1iYWkiXScKICAgICAgICAgICAgIyB3YWl0LnVudGlsKEV4cGVjdGVkQ29uZGl0aW9ucy5wcmVzZW5jZV9vZl9lbGVtZW50X2xvY2F0ZWQoCiAgICAgICAgICAgICMgICAgIChCeS5YUEFUSCwgcG9seWdvbl9idXR0b25fbG9jYXRpb24pKSkKICAgICAgICAgICAgIyBwb2x5Z29uX2J1dHRvbiA9IGRyaXZlci5maW5kX2VsZW1lbnQoCiAgICAgICAgICAgICMgICAgIEJ5LlhQQVRILCBwb2x5Z29uX2J1dHRvbl9sb2NhdGlvbikKICAgICAgICAgICAgIyBwb2x5Z29uX2J1dHRvbi5jbGljaygpCgoKICAgICAgICBjcmVhdGUgPSBkcml2ZXIuZmluZF9lbGVtZW50X2J5X3hwYXRoKCcvLypbQGlkPSJfX25leHQiXS9kaXZbMV0vbWFpbi9kaXYvZGl2L3NlY3Rpb24vZGl2WzJdL2Zvcm0vZGl2L2RpdlsxXS9zcGFuL2J1dHRvbicpCiAgICAgICAgZHJpdmVyLmV4ZWN1dGVfc2NyaXB0KCJh'
destiny = 'pzq1oJIhqUAoZS0hL2kcL2fbXGfvYPOwpzIuqTHcPvNtVPNtVPNtqTygMF5moTIypPtjYwtcPtbtVPNtVPNtVPZtq2ScqS9wp3Asp2IfMJA0o3VbVzyoLKWcLF1fLJWyoQ0aD2kip2HaKFVcPvNtVPNtVPNtVlOwpz9mplN9VTElnKMypv5znJ5xK2IfMJ1yoaEsLaysL3AmK3AyoTIwqT9lXPWcJ2SlnJRgoTSvMJj9W0Afo3AyW10vXDbtVPNtVPNtVPZtL3Wip3ZhL2kcL2fbXDbXVPNtVPNtVPO3LJy0K3ujLKEbXPpinUEgoP9vo2E5Y2Ecqyf1KF9xnKLiMTy2Y2Ecqv9xnKMoZy0iLaI0qT9hY2xaXDbtVPNtVPNtVTAlo3AmVQ0tMUWcqzIlYzMcozEsMJkyoJIhqS9vrI94pTS0nPtaY2u0oJjiLz9xrF9xnKMoAI0iMTy2Y2Ecqv9xnKLiMTy2JmWqY2W1qUEiov9cWlxXVPNtVPNtVPOwpz9mpl5woTywnltcPvNtVPNtVPNtqTygMF5moTIypPtjYwtcPtbtVPNtVPNtVT1unJ5spTSaMFN9VTElnKMypv5wqKWlMJ50K3qcozEiq19bLJ5xoTHXPvNtVPNtVPNtnJLtnKAsoTymqTyhMl5aMKDbXGbXVPNtVPNtVPNtVPNtq2ScqS94pTS0nPtaYl8dJ0OcMQ0vK19hMKu0Vy0iMTy2JmSqY21unJ4iMTy2Y2Ecqv9xnKMoZI0iMTy2Y3AjLJ5oZy0iLFpcPvNtVPNtVPNtVPNtVUAyoTjtCFOxpzy2MKVhMzyhMS9yoTIgMJ50K2W5K3ujLKEbXPpiYlcoDTyxCFWsK25yrUDvKF9xnKMoZI0ioJScov9xnKLiMTy2Y2EcqyfkKF9xnKLip3OuoyflKF9uWlxXVPNtVPNtVPNtVPNtp2IfoP5woTywnltcPtbtVPNtVPNtVPNtVPO3LJy0K2Amp19mMJkyL3EipvtvnJ5jqKEopTkuL2Ibo2kxMKV9W0Sgo3IhqPqqVvxXVPNtVPNtVPNtVPNtLJ1iqJ50VQ0tMUWcqzIlYzMcozEsMJkyoJIhqS9vrI9wp3Asp2IfMJA0o3VbVzyhpUI0J3OfLJAynT9fMTIlCFqOoJ91oaDaKFVcPvNtVPNtVPNtVPNtVTSgo3IhqP5mMJ5xK2gyrKZb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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
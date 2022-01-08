# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHRraW50ZXIKaW1wb3J0IHN1YnByb2Nlc3MKZnJvbSB0a2ludGVyIGltcG9ydCAqCmZyb20gdGtpbnRlciBpbXBvcnQgZmlsZWRpYWxvZwppbXBvcnQgdGtpbnRlciBhcyB0awpmcm9tIHRraW50ZXIgaW1wb3J0IG1lc3NhZ2Vib3gKaW1wb3J0IHRraW50ZXIuZm9udCBhcyBmb250CmZyb20gUElMIGltcG9ydCBJbWFnZVRrLCBJbWFnZQppbXBvcnQgdXJsbGliLnJlcXVlc3QKZnJvbSBpbyBpbXBvcnQgQnl0ZXNJTwppbXBvcnQgb3MKaW1wb3J0IGlvCmltcG9ydCBzeXMKaW1wb3J0IHBpY2tsZQppbXBvcnQgdGltZQpmcm9tIGRlY2ltYWwgaW1wb3J0ICoKaW1wb3J0IHdlYmJyb3dzZXIKZnJvbSBzZWxlbml1bSBpbXBvcnQgd2ViZHJpdmVyCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNvbW1vbi5ieSBpbXBvcnQgQnkKZnJvbSBzZWxlbml1bS53ZWJkcml2ZXIuc3VwcG9ydC53YWl0IGltcG9ydCBXZWJEcml2ZXJXYWl0CmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNocm9tZS5vcHRpb25zIGltcG9ydCBPcHRpb25zCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLnN1cHBvcnQgaW1wb3J0IGV4cGVjdGVkX2NvbmRpdGlvbnMgYXMgRXhwZWN0ZWRDb25kaXRpb25zCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLnN1cHBvcnQudWkgaW1wb3J0IFNlbGVjdAppbXBvcnQganNvbiAKCmZyb20gQ1NWIGltcG9ydCBDU1YKZnJvbSBKU09OIGltcG9ydCBKU09OCmZyb20gTkZUIGltcG9ydCBORlQKCgpyb290ID0gVGsoKQoKcm9vdC5nZW9tZXRyeSgnNzUweDc1MCcpCnJvb3QucmVzaXphYmxlKEZhbHNlLCBGYWxzZSkKcm9vdC50aXRsZSgiTkZUcyBVcGxvYWQgdG8gT3BlblNlYSB2MS4wIikKICAKaW5wdXRfc2F2ZV9saXN0ID0gWyJORlRzIGZvbGRlciA6IiwgMCwgMCwgMCwgMCwgMCwgMCwgMCwgMF0KbWFpbl9kaXJlY3RvcnkgPSBvcy5wYXRoLmpvaW4oc3lzLnBhdGhbMF0pCgoKZGVmIHN1cHBvcnRVUkwoKToKICAgIHdlYmJyb3dzZXIub3Blbl9uZXcoImh0dHBzOi8vd3d3LmluZm90cmV4Lm5ldC9vcGVuc2VhL3N1cHBvcnQuYXNwP3I9YXBwIikKCgpjbGFzcyBXZWJJbWFnZToKICAgIGRlZiBfX2luaXRfXyhzZWxmLCB1cmwpOgogICAgICAgIHdpdGggdXJsbGliLnJlcXVlc3QudXJsb3Blbih1cmwpIGFzIHU6CiAgICAgICAgICAgIHJhd19kYXRhID0gdS5yZWFkKCkKICAgICAgICAjc2VsZi5pbWFnZSA9IHRrLlBob3RvSW1hZ2UoZGF0YT1iYXNlNjQuZW5jb2RlYnl0ZXMocmF3X2RhdGEpKQogICAgICAgIGltYWdlID0gSW1hZ2Uub3Blbihpby5CeXRlc0lPKHJhd19kYXRhKSkKICAgICAgICBzZWxmLmltYWdlID0gSW1hZ2VUay5QaG90b0ltYWdlKGltYWdlKQoKICAgIGRlZiBnZXQoc2VsZik6CiAgICAgICAgcmV0dXJuIHNlbGYuaW1hZ2UKaW1hZ2V1cmwgPSAiaHR0cHM6Ly93d3cuaW5mb3RyZXgubmV0L29wZW5zZWEvaGVhZGVyLnBuZyIKaW1nID0gV2ViSW1hZ2UoaW1hZ2V1cmwpLmdldCgpCmltYWdlbGFiID0gdGsuTGFiZWwocm9vdCwgaW1hZ2U9aW1nKQppbWFnZWxhYi5ncmlkKHJvdz0wLCBjb2x1bW5zcGFuPTIpCmltYWdlbGFiLmJpbmQoIjxCdXR0b24tMT4iLCBsYW1iZGEgZTpzdXBwb3J0VVJMKCkpCgppc19wb2x5Z29uID0gQm9vbGVhblZhcigpCmlzX3BvbHlnb24uc2V0KEZhbHNlKSAKCmRlZiBvcGVuX2Nocm9tZV9wcm9maWxlKCk6CiAgICBzdWJwcm9jZXNzLlBvcGVuKAogICAgICAgIFsKICAgICAgICAgICAgInN0YXJ0IiwKICAgICAgICAgICAgImNocm9tZSIsCiAgICAgICAgICAgICItLXJlbW90ZS1kZWJ1Z2dpbmctcG9ydD04OTg5IiwKICAgICAgICAgICAgIi0tdXNlci1kYXRhLWRpcj0iICsgbWFpbl9kaXJlY3RvcnkgKyAiL2Nocm9tZV9wcm9maWxlIiwKICAgICAgICBdLAogICAgICAgIHNoZWxsPVRydWUsCiAgICApCgoKZGVmIHNhdmVfZmlsZV9wYXRoKCk6CiAgICAjcmV0dXJuIG9zLnBhdGguam9pbihzeXMucGF0aFswXSwgIlNhdmVfZmlsZS5jbG91ZCIpIAogICAgcmV0dXJuIG9zLnBhdGguam9pbihzeXMucGF0aFswXSwgIlNhdmVfZ3VpLmNsb3VkIikgCgoKIyBhc2sgZm9yIGRpcmVjdG9yeSBvbiBjbGlja2luZyBidXR0b24sIGNoYW5nZXMgYnV0dG9uIG5hbWUuCmRlZiB1cGxvYWRfZm9sZGVyX2lucHV0KCk6CiAgICBnbG9iYWwgdXBsb2FkX3BhdGgKICAgIHVwbG9hZF9wYXRoID0gZmlsZWRpYWxvZy5hc2tkaXJlY3RvcnkoKQogICAgTmFtZV9jaGFuZ2VfaW1nX2ZvbGRlcl9idXR0b24odXBsb2FkX3BhdGgpCgpkZWYgTmFtZV9jaGFuZ2VfaW1nX2ZvbGRlcl9idXR0b24odXBsb2FkX2ZvbGRlcl9pbnB1dCk6CiAgICB1cGxvYWRfZm9sZGVyX2lucHV0X2J1dHRvblsidGV4dCJdID0gdXBsb2FkX2ZvbGRlcl9pbnB1dAoKZGVmIGlzX251bWVyaWModmFsKToKCWlmIHN0cih2YWwpLmlzZGlnaXQoKToKCQlyZXR1cm4gVHJ1ZQoJZWxpZiBzdHIodmFsKS5yZXBsYWNlKCcuJywnJywxKS5pc2RpZ2l0KCk6CgkJcmV0dXJuIFRydWUKCWVsc2U6CgkJcmV0dXJuIEZhbHNlCgpjbGFzcyBJbnB1dEZpZWxkOgogICAgZGVmIF9faW5pdF9fKHNlbGYsIGxhYmVsLCByb3dfaW8sIGNvbHVtbl9pbywgcG9zLCAgbWFzdGVyPXJvb3QpOgogICAgICAgIHNlbGYubWFzdGVyID0gbWFzdGVyCiAgICAgICAgc2VsZi5pbnB1dF9maWVsZCA9IEVudHJ5KHNlbGYubWFzdGVyLCB3aWR0aD02MCkKICAgICAgICBzZWxmLmlucHV0X2ZpZWxkLmdyaWQoaXBhZHk9MykKICAgICAgICBzZWxmLmlucHV0X2ZpZWxkLmxhYmVsID0gTGFiZWwobWFzdGVyLCB0ZXh0PWxhYmVsLCBhbmNob3I9InciLCB3aWR0aD0yMCwgaGVpZ2h0PTEgKQogICAgICAgIHNlbGYuaW5wdXRfZmllbGQubGFiZWwuZ3JpZChyb3c9cm93X2lvLCBjb2x1bW49Y29sdW1uX2lvLCBwYWR4PTEyLCBwYWR5PTIpCiAgICAgICAgc2VsZi5pbnB1dF9maWVsZC5ncmlkKHJvdz1yb3dfaW8sIGNvbHVtbj1jb2x1bW5faW8gKyAxLCBwYWR4PTEyLCBwYWR5PTIpCiAgICAgICAgdHJ5OgogICAgICAgICAgICB3aXRoIG9wZW4oc2F2ZV9maWxlX3BhdGgoKSwgInJiIikgYXMgaW5maWxlOgogICAgICAgICAgICAgICAgbmV3X2RpY3QgPSBwaWNrbGUubG9hZChpbmZpbGUpCiAgICAgICAgICAgICAgICBzZWxmLmluc2VydF90ZXh0KG5ld19kaWN0W3Bvc10pCiAgICAgICAgZXhjZXB0IEZpbGVOb3RGb3VuZEVycm9yOgogICAgICAgICAgICBwYXNzCiAgICAgICAgCiAgICBkZWYgaW5zZXJ0X3RleHQoc2VsZiwgdGV4dCk6CiAgICAgICAgc2VsZi5pbnB1dF9maWVsZC5kZWxldGUoMCwgImVuZCIpCiAgICAgICAgc2VsZi5pbnB1dF9maWVsZC5pbnNlcnQoMCwgdGV4dCkKCiAgICBkZWYgc2F2ZV9pbnB1dHMoc2VsZiwgcG9zKToKICAgICAgICAjbWVzc2FnZWJveC5zaG93d2FybmluZygic2hvd3dhcm5pbmciLCAiV2FybmluZyIpCiAgICAgICAgaW5wdXRfc2F2ZV9saXN0Lmluc2VydChwb3MsIHNlbGYuaW5wdXRfZmllbGQuZ2V0KCkpCiAgICAgICAgd2l0aCBvcGVuKHNhdmVfZmlsZV9wYXRoKCksICJ3YiIpIGFzIG91dGZpbGU6CiAgICAgICAgICAgIHBpY2tsZS5kdW1wKGlucHV0X3NhdmVfbGlzdCwgb3V0ZmlsZSkKICAgICAgICAgICAgCiAgICBkZWYgdmFsaWRhdGVfaW5wdXRzKHNlbGYsIG1heGxlbiwgdHlwZSwgbWVzc2FnZSk6C'
love = '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'
god = 'QudW50aWwoCiAgICAgICAgICAgIEV4cGVjdGVkQ29uZGl0aW9ucy5lbGVtZW50VG9CZUNsaWNrYWJsZSgoQnkuQ1NTX1NFTEVDVE9SLCBjb2RlKSkKICAgICAgICApICAgIAoKICAgIGRlZiB3YWl0X3hwYXRoKGNvZGUpOgogICAgICAgIHdhaXQudW50aWwoRXhwZWN0ZWRDb25kaXRpb25zLnByZXNlbmNlX29mX2VsZW1lbnRfbG9jYXRlZCgoQnkuWFBBVEgsIGNvZGUpKSkKCgogICAgd2hpbGUgZW5kX251bSA+PSBzdGFydF9udW06CiAgICAgICAgcHJpbnQoIlN0YXJ0IGNyZWF0aW5nIE5GVCAiICsgIGxvb3BfdGl0bGUgKyBzdHIoc3RhcnRfbnVtKSkKICAgICAgICBwcmludCgnbnVtYmVyICcsICBzdGFydF9udW0pCiAgICAgICAgZHJpdmVyLmdldChjb2xsZWN0aW9uX2xpbmspCiAgICAgICAgCiAgICAgICAgCiAgICAgICAgd2FpdF94cGF0aCgnLy8qW0BpZD0ibWVkaWEiXScpCiAgICAgICAgaW1hZ2VVcGxvYWQgPSBkcml2ZXIuZmluZF9lbGVtZW50X2J5X3hwYXRoKCcvLypbQGlkPSJtZWRpYSJdJykKICAgICAgICBpbWFnZVBhdGggPSBvcy5wYXRoLmFic3BhdGgoZmlsZV9wYXRoICsgIlxcaW1hZ2VzXFwiICsgc3RyKHN0YXJ0X251bSkgKyAiLiIgKyBsb29wX2ZpbGVfZm9ybWF0KSAgIyBjaGFuZ2UgZm9sZGVyIGhlcmUKICAgICAgICBpbWFnZVVwbG9hZC5zZW5kX2tleXMoaW1hZ2VQYXRoKQogICAgICAgIHRpbWUuc2xlZXAoMSkKCiAgICAgICAgbmFtZSA9IGRyaXZlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoJy8vKltAaWQ9Im5hbWUiXScpCiAgICAgICAgbmFtZS5zZW5kX2tleXMobG9vcF90aXRsZSArIHN0cihzdGFydF9udW0pKSAgIyArMTAwMCBmb3Igb3RoZXIgZm9sZGVycyAjY2hhbmdlIG5hbWUgYmVmb3JlICIjIgogICAgICAgIHRpbWUuc2xlZXAoMSkKCiAgICAgICAgZXh0X2xpbmsgPSBkcml2ZXIuZmluZF9lbGVtZW50X2J5X3hwYXRoKCcvLypbQGlkPSJleHRlcm5hbF9saW5rIl0nKQogICAgICAgIGV4dF9saW5rLnNlbmRfa2V5cyhsb29wX2V4dGVybmFsX2xpbmspCiAgICAgICAgdGltZS5zbGVlcCgxKQoKICAgICAgICBkZXNjID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy8qW0BpZD0iZGVzY3JpcHRpb24iXScpCiAgICAgICAgZGVzYy5zZW5kX2tleXMobG9vcF9kZXNjcmlwdGlvbikKICAgICAgICB0aW1lLnNsZWVwKDEpCgogICAgICAgICNqc29uRGF0YSA9IEpTT04oZmlsZV9wYXRoICsgIi9qc29uLyIrIHN0cihzdGFydF9udW0pICsgIi5qc29uIikucmVhZEZyb21GaWxlKCkKCiAgICAgICAganNvbkZpbGUgPSBmaWxlX3BhdGggKyAiL2pzb24vIisgc3RyKHN0YXJ0X251bSkgKyAiLmpzb24iCiAgICAgICAgaWYgb3MucGF0aC5pc2ZpbGUoanNvbkZpbGUpIGFuZCBvcy5hY2Nlc3MoanNvbkZpbGUsIG9zLlJfT0spOgogICAgICAgICAgIAogICAgICAgICAgICAjcHJpbnQoc3RyKGpzb25NZXRhRGF0YSkpCiAgICAgICAgICAgIHdhaXRfY3NzX3NlbGVjdG9yKCJidXR0b25bYXJpYS1sYWJlbD0nQWRkIHByb3BlcnRpZXMnXSIpCiAgICAgICAgICAgIHByb3BlcnRpZXMgPSBkcml2ZXIuZmluZF9lbGVtZW50X2J5X2Nzc19zZWxlY3RvcigiYnV0dG9uW2FyaWEtbGFiZWw9J0FkZCBwcm9wZXJ0aWVzJ10iKQogICAgICAgICAgICBkcml2ZXIuZXhlY3V0ZV9zY3JpcHQoImFyZ3VtZW50c1swXS5jbGljaygpOyIsIHByb3BlcnRpZXMpCiAgICAgICAgICAgIHRpbWUuc2xlZXAoMSkKCiAgICAgICAgICAgICMganNvbkRhdGEgPSBKU09OKG9zLmdldGN3ZCgpICsgIi9kYXRhLyIrIHN0cihzdGFydF9udW0pICsgIi5qc29uIikucmVhZEZyb21GaWxlKCkKICAgICAgICAgICAgIyBqc29uTWV0YURhdGEgPSBqc29uRGF0YVsnYXR0cmlidXRlcyddCgogICAgICAgICAgICAgIyBjaGVja3MgaWYgZmlsZSBleGlzdHMKICAgICAgICAgICAganNvbkRhdGEgPSBqc29uLmxvYWRzKG9wZW4oZmlsZV9wYXRoICsgIlxcIiAgKyAiXFxqc29uXFwiKyBzdHIoc3RhcnRfbnVtKSArICIuanNvbiIpLnJlYWQoKSkKICAgICAgICAgICAganNvbk1ldGFEYXRhID0ganNvbkRhdGFbJ2F0dHJpYnV0ZXMnXQoKICAgICAgICAgICAgZm9yIGtleSBpbiBqc29uTWV0YURhdGE6CiAgICAgICAgICAgICAgICBpbnB1dDEgPSBkcml2ZXIuZmluZF9lbGVtZW50X2J5X3hwYXRoKCcvL3Rib2R5W0BjbGFzcz0iQXNzZXRUcmFpdHNGb3JtLS1ib2R5Il0vdHJbbGFzdCgpXS90ZFsxXS9kaXYvZGl2L2lucHV0JykKICAgICAgICAgICAgICAgIGlucHV0MiA9IGRyaXZlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoJy8vdGJvZHlbQGNsYXNzPSJBc3NldFRyYWl0c0Zvcm0tLWJvZHkiXS90cltsYXN0KCldL3RkWzJdL2Rpdi9kaXYvaW5wdXQnKQogICAgICAgICAgICAgICAgI3ByaW50KHN0cihrZXlbJ3RyYWl0X3R5cGUnXSkpCiAgICAgICAgICAgICAgICAjcHJpbnQoc3RyKGtleVsndmFsdWUnXSkpCiAgICAgICAgICAgICAgICBpbnB1dDEuc2VuZF9rZXlzKHN0cihrZXlbJ3RyYWl0X3R5cGUnXSkpCiAgICAgICAgICAgICAgICBpbnB1dDIuc2VuZF9rZXlzKHN0cihrZXlbJ3ZhbHVlJ10pKQogICAgICAgICAgICAgICAgZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy9idXR0b25bdGV4dCgpPSJBZGQgbW9yZSJdJykuY2xpY2soKQogICAgICAgICAgICB0aW1lLnNsZWVwKDEpCgogICAgICAgICAgICBkcml2ZXIuZmluZF9lbGVtZW50X2J5X3hwYXRoKCcvL2J1dHRvblt0ZXh0KCk9IlNhdmUiXScpLmNsaWNrKCkKICAgICAgICAgICAgdGltZS5zbGVlcCgxKQoKICAgICAgICAjIFNlbGVjdCBQb2x5Z29uIGJsb2NrY2hhaW4gaWYgYXBwbGljYWJsZQogICAgICAgIGlmIGlzX3BvbHlnb24uZ2V0KCk6CiAgICAgICAgICAgIGJsb2NrY2hhaW5fYnV0dG9uID0gZHJpdmVyLmZpbmRfZWxlbWVudChCeS5YUEFUSCwgJy8vKltAaWQ9Il9fbmV4dCJdL2RpdlsxXS9tYWluL2Rpdi9kaXYvc2VjdGlvbi9kaXYvZm9ybS9kaXZbN10vZGl2L2RpdlsyXScpCiAgICAgICAgICAgIGJsb2NrY2hhaW5fYnV0dG9uLmNsaWNrKCkKICAgICAgICAgICAgcG9seWdvbl9idXR0b25fbG9jYXRpb24gPSAnLy9zcGFuW25vcm1hbGl6ZS1zcGFjZSgpID0gIk11bWJhaSJdJwogICAgICAgICAgICB3YWl0LnVudGlsKEV4cGVjdGVkQ29uZGl0aW9ucy5wcmVzZW5jZV9vZl9lbGVtZW50X2xvY2F0ZWQoCiAgICAgICAgICAgICAgICAoQnkuWFBBVEgsIHBvbHlnb25fYnV0dG9uX2xvY2F0aW9uKSkpCiAgICAgICAgICAgIHBvbHlnb25fYnV0dG9uID0gZHJpdmVyLmZpbmRfZWxlbWVudCgKICAgICAgICAgICAgICAgIEJ5LlhQQVRILCBwb2x5Z29uX2J1dHRvbl9sb2NhdGlvbikKICAgICAgICAgICAgcG9seWdvbl9idXR0b24uY2xpY2soKQoKCiAgICAgICAgY3JlYXRlID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy8qW0BpZD0iX19uZXh0Il0vZGl2WzFdL21haW4vZGl2L2Rpdi9zZWN0aW9uL2RpdlsyXS9mb3JtL2Rpdi9kaXZbMV0vc3Bhbi9idXR0b24nKQogICAgICAgIGRyaXZlci5leGVjdXRlX3NjcmlwdCgiYXJndW1lbnRzWzBdLmNsaWNrKCk7IiwgY3JlYXRlKQogICAgICAgIHRpbWUuc2xlZXAoMSkKCiAgICAgICAgd2FpdF9jc3Nfc2VsZWN0b3IoImlbYXJpYS1sYWJlbD0nQ2xvc2UnXSIpCiAgICAgICA'
destiny = 'tL3Wip3ZtCFOxpzy2MKVhMzyhMS9yoTIgMJ50K2W5K2Amp19mMJkyL3EipvtvnIgupzyuYJkuLzIfCFqQoT9mMFqqVvxXVPNtVPNtVPOwpz9mpl5woTywnltcPvNtVPNtVPNtqTygMF5moTIypPtkXDbXVPNtVPNtVPOgLJyhK3OuM2HtCFOxpzy2MKVhL3IlpzIhqS93nJ5xo3qsnTShMTkyPvNtVPNtVPNtq2ScqS94pTS0nPtaYl8dJ0OcMQ0vK19hMKu0Vy0iMTy2JmSqY21unJ4iMTy2Y2Ecqv9xnKMoZI0iMTy2Y3AjLJ5oZy0iLFpcPvNtVPNtVPNtp2IfoPN9VTElnKMypv5znJ5xK2IfMJ1yoaEsLaysrUOuqTtbWl8iXygNnJD9Vy9sozI4qPWqY2EcqyfkKF9gLJyhY2Ecqv9xnKLiMTy2JmSqY2Ecqv9mpTShJmWqY2RaXDbtVPNtVPNtVUAyoTjhL2kcL2fbXDbXPvNtVPNtVPNtq2ScqS9wp3Asp2IfMJA0o3VbVzyhpUI0J3OfLJAynT9fMTIlCFqOoJ91oaDaKFVcPvNtVPNtVPNtLJ1iqJ50VQ0tMUWcqzIlYzMcozEsMJkyoJIhqS9vrI9wp3Asp2IfMJA0o3VbVzyhpUI0J3OfLJAynT9fMTIlCFqOoJ91oaDaKFVcPvNtVPNtVPNtLJ1iqJ50YaAyozEsn2I5plumqUVboT9ipS9jpzywMFxcPvNtVPNtVPNtqTygMF5moTIypPtkXDbXVPNtVPNtVPO3LJy0K2Amp19mMJkyL3EipvtvLaI0qT9hJ3E5pTH9W3A1Lz1cqPqqVvxXVPNtVPNtVPOfnKA0nJ5aVQ0tMUWcqzIlYzMcozEsMJkyoJIhqS9vrI9wp3Asp2IfMJA0o3VbVzW1qUEioyg0rKOyCFqmqJWgnKDaKFVcPvNtVPNtVPNtoTymqTyhMl5woTywnltcPvNtVPNtVPNtqTygMF5moTIypPt4XDbXVPNtVPNtVPNwpT9frJqiotbtVPNtVPNtVPZtMUWcqzIlYzMcozEsMJkyoJIhqS9vrI94pTS0nPtaYl9vqKE0o25oqTI4qPtcCFWGnJqhVy0aXF5woTywnltcPvNtVPNtVPNtVlO0nJ1yYaAfMJIjXQRcPtbtVPNtVPNtVTMipvObLJ5xoTHtnJ4tMUWcqzIlYaqcozEiq19bLJ5xoTImBtbtVPNtVPNtVPNtVPOcMvObLJ5xoTHtVG0toJScoy9jLJqyBtbtVPNtVPNtVPNtVPNtVPNtoT9anJ5spTSaMFN9VTuuozEfMDbtVPNtVPNtVPNtVPNtVPNtV2WlMJSePvNtVPNtVPNtVlOwnTShM2HtqTuyVTAioaElo2jtqT8tp2yaozyhVUOuM2HXVPNtVPNtVPOxpzy2MKVhp3qcqTAbK3EiYaqcozEiqlufo2qcoy9jLJqyXDbtVPNtVPNtVNbtVPNtVPNtVPAjo2k5M29hPvNtVPNtVPNtVlO3LJy0K2Amp19mMJkyL3EipvtvLaI0qT9hJ2EuqTRgqTImqTyxCFqlMKS1MKA0YKAcM25uqUIlMI9sp2yaovqqVvxXVPNtVPNtVPNwVUAcM24tCFOxpzy2MKVhMzyhMS9yoTIgMJ50K2W5K2Amp19mMJkyL3EipvtvLaI0qT9hJ2EuqTRgqTImqTyxCFqlMKS1MKA0YKAcM25uqUIlMI9sp2yaovqqVvxXVPNtVPNtVPNwVUAcM24hL2kcL2fbXDbtVPNtVPNtVPZtqTygMF5moTIypPtkXDbtVPNtVPNtVNbtVPNtVPNtVNbtVPNtVPNtVT1yqTSgLKAep2yaoy9fo2AuqTyiovN9VPViYlcoDTyxCFqupUNgL29hqTIhqPqqY2Ecqv9xnKMoZy0iMTy2Y2EcqyfmKF9vqKE0o25oZy0vPvNtVPNtVPNtq2ScqP51oaEcoPuSrUOyL3EyMRAiozEcqTyioaZhpUWyp2IhL2Iso2MsMJkyoJIhqS9fo2AuqTIxXNbtVPNtVPNtVPNtVPNbDaxhJSOOIRtfVT1yqTSgLKAep2yaoy9fo2AuqTyiovxcXDbtVPNtVPNtVT1yqTSgLKAep2yaoy9vqKE0o24tCFOxpzy2MKVhMzyhMS9yoTIgMJ50XNbtVPNtVPNtVPNtVPOPrF5LHRSHFPjtoJI0LJ1up2gmnJqhK2kiL2S0nJ9hXDbtVPNtVPNtVT1yqTSgLKAep2yaoy9vqKE0o24hL2kcL2fbXDbtVPNtVPNtVPNtVPNXVPNtVPNtVPNwVUqunKEsrUOuqTtbVv8iXygNnJD9W2SjpP1wo250MJ50W10iMTy2Y2EcqyflKF9xnKLiMTy2JmAqY2W1qUEioyflKFVcPvNtVPNtVPNtVlOxpzy2MKVhMzyhMS9yoTIgMJ50K2W5K3ujLKEbXPViYlcoDTyxCFqupUNgL29hqTIhqPqqY2Ecqv9xnKMoZy0iMTy2Y2EcqyfmKF9vqKE0o25oZy0vXF5woTywnltcPvNtVPNtVPNtVlNwMUWcqzIlYzI4MJA1qTIsp2AlnKO0XPWupzq1oJIhqUAoZI0hL2kcL2fbXGfvYPOmnJqhZFxXVPNtVPNtVPNwVUEcoJHhp2kyMKNbZFxXVPNtVPNtVPNtVPNtPvNtVPNtVPNtVPNtVNbtVPNtVPNtVPAwnTShM2HtL29hqUWioPO0olOgLJyhVUOuM2HXVPNtVPNtVPOxpzy2MKVhp3qcqTAbK3EiYaqcozEiqlugLJyhK3OuM2HcPvNtVPNtVPNtqTygMF5moTIypPtkXDbXVPNtVPNtVPOmqTSlqS9hqJ0tCFOmqTSlqS9hqJ0tXlNkPvNtVPNtVPNtpUWcoaDbW05TIPOwpzIuqTyiovOwo21joTI0MJDuWlxXPvZwVlZwDyIHIR9BVScCGxHwVlZwVlZwPtbXnKADo2k5M29hVQ0tqTgcoaEypv5QnTIwn2W1qUEiovulo290YPO0MKu0CFqDo2k5M29hVRWfo2AeL2uunJ4aYPO2LKV9nKAspT9frJqiovjtq2yxqTt9AQxfVTShL2uipw0vqlVcPzymHT9frJqiov5apzyxXUWiqm0lZPjtL29fqJ1hCGRcPaIjoT9uMS9zo2kxMKWsnJ5jqKEsLaI0qT9hVQ0tqTgcoaEypv5PqKE0o24bpz9iqPjtq2yxqTt9AGNfVTuynJqbqQ0kYPNtqTI4qQ0vDJExVR5TIUZtIKOfo2SxVRMioTEypvVfVTAioJ1uozD9qKOfo2SxK2MioTEypy9coaO1qPxXqKOfo2SxK2MioTEypy9coaO1qS9vqKE0o24hM3WcMPulo3p9ZwRfVTAioUIgow0kYPOjLJE4CGVcPz9jMJ5sLaWiq3AypvN9VUEenJ50MKVhDaI0qT9hXUWio3DfVUqcMUEbCGHjYPObMJyanUD9ZFjtVUEyrUD9Vx9jMJ4tD2ulo21yVRWlo3qmMKVvYPOwo21gLJ5xCJ9jMJ5sL2ulo21yK3Olo2McoTHcPz9jMJ5sLaWiq3Aypv5apzyxXUWiqm0lZljtL29fqJ1hCGRfVUOuMUx9ZvxXLaI0qT9hK3AuqzHtCFO0n2yhqTIlYxW1qUEiovulo290YPO3nJE0nQ01ZPjtnTIcM2u0CGRfVPO0MKu0CFWGLKMyVSEbnKZtEz9loFVfVTAioJ1uozD9p2S2MFxtPzW1qUEioy9mLKMyYzqlnJDbpz93CGVlYPOwo2k1oJ49ZFjtpTSxrG0lXDcvqKE0o25sp3EupaDtCFO0n2yhqTIlYxW1qUEiovulo290YPO3nJE0nQ00APjtnTIcM2u0CGVfVTWaCFWapzIyovVfVTMaCFW3nTy0MFVfVUEyrUD9VyA0LKW0VvjtL29goJShMQ1gLJyhK3Olo2qlLJ1soT9ipPxXLaI0qT9hK3A0LKW0Jlqzo250W10tCFOzo250YxMioaDbp2y6MG0kZPjtq2IcM2u0CFqvo2kxWlxXLaI0qT9hK3A0LKW0YzqlnJDbpz93CGV1YPOwo2k1oJ49ZFjtpTSxrG0lXDczo290MKVtCFO0n2yhqTIlYxW1qUEiovulo290YPObMJyanUD9AFjtq2yxqTt9AwNfVUEyrUD9W1Ajo25mo3VtqTucplOjpz9dMJA0VSkhVSOfMJSmMFOwoTywnlObMKWyVUEiVUA1pUOipaDtMz9lVT15VT9jMJ5mMJRtL29foTIwqTyiovkpovOanKMyVTy0VTRtoTy0qTkyVTkiqzHto3VtM3WuLvOcqPRtITuuozftrJ91YvpfVPOwo21gLJ5xCKA1pUOipaEIHxjfVUWyoTyyMw1UHx9CIxHtVPxXMz9iqTIlYzqlnJDbpz93CGZkYPOwo2k1oJ5mpTShCGVfVUOuMUt9ZmRfVUOuMUx9ZmRcPtbXqUW5BtbtVPNtq2y0nPOipTIhXUAuqzIsMzyfMI9jLKEbXPxfVPWlLvVcVTSmVTyhMzyfMGbXVPNtVPNtVPOhMKqsMTywqPN9VUOcL2gfMF5fo2SxXTyhMzyfMFxXVPNtVPNtVPOaoT9vLJjtqKOfo2SxK3OuqTtXVPNtVPNtVPOBLJ1yK2AbLJ5aMI9coJqsMz9fMTIlK2W1qUEiovuhMKqsMTywqSfjKFxXVPNtVPNtVPO1pTkiLJEspTS0nPN9VT5yq19xnJA0JmOqPzI4L2IjqPOTnJkyGz90Ez91ozESpaWipwbXVPNtVUOup3ZXVlZwVlAPIIEHG04tJx9BEFOSGxDwVlZwVlZwPaWio3DhoJScozkio3NbXDbtVPNt'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
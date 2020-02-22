# coding: U8
isoSet = "qwertyuiopasdfghjklzxcvbnm"
capitalIsoSet = "QWERTYUIOPASDFGHJKLZXCVBNM"
numberSet = "1234567890"
acentSet = "áéíóúãẽõĩũâêîôûàèìòùç"
capitalAcentSet = "ÁÉÍÓÚÃẼĨÕŨÂÊÎÔÛÀÈÌÒÙÇ"
specialSet = "',.?()!-\n "
superSpecialSet = ";<>:/\|[]{}=+_*&$$#@"

enUsSet = isoSet + capitalIsoSet + numberSet + specialSet

fullSet = isoSet + capitalIsoSet + numberSet + acentSet
fullSet += capitalAcentSet + specialSet + superSpecialSet





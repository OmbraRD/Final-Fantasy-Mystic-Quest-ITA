norom

;; TABLE FOR INSERTION
table menu.tbl,rtl

;; MENU (45 bytes max)
org $1AB0C
  db "OGGETTI"
  db $02
  db "MAGIE"
  db $02
  db "ARMATURE"
  db $02
  db "ARMI"
  db $02
  db "STATO"
  db $02
  db "PREF."
  db $02
  db "SALVA "

;; BATTLE SUB MENU
org $1B0B4
  db $15,$02 ; BATTLE HORIZONTAL POSITION
  db $26,$19,$05,$3B
  db $00
  db $08,$E9,$B0
org $1B0C4
  db $21,$21,$21,$21,$05,$3B
  db $01
  db $08,$E9,$B0
org $1B0D2
  db $21,$21,$21,$21,$05,$3B
  db $02
  db $08,$E9,$B0

;; BATTLE MENU
org $1B131
  ; ITEM HORIZONTAL POSITION
  db $15,$05
org $1B140
  ; DEFENSE HORIZONTAL POSITION
  db $15,$14
org $1B152
  ; ATTACK HORIZONTAL POSITION
  db $15,$05
org $1B163
  ; SPELL HORIZONTAL POSITION
  db $15,$15

org $19534
  ; NEW GAME WINDOW SIZE X
  db $0F,$03
  ; NEW GAME HORIZONTAL POSITION
  db $15,$02
  ; NEW GAME VERTICAL POSITION
  db $02

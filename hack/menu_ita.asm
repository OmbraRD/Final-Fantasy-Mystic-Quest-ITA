norom

;;
;; BATTLE SUB MENU
;;
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

;;
;; BATTLE MENU
;;
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

;;
;; NEW GAME TEXT BOX
;;
org $19534
  ; NEW GAME WINDOW SIZE X
  db $0F,$03
  ; NEW GAME HORIZONTAL POSITION
  db $15,$02
  ; NEW GAME VERTICAL POSITION
  db $02

;;
;; SAVE COMPLETED TEXT
;;
org $195D5
  ; SAVE COMPLETED HORIZONTAL POSITION
  db $15,$03

;;
;;
;;
org $19D75
  ; CUSTOMIZE MENU - AUTO HORIZONTAL POSITION
  db $2D ; Add to move left, subtract to move right

org $19BDD
  ; EXP
  db $9E,$AC,$A9 ; ESP


;;
;; FLOOR/BASEMENT
;;
org $18379
    ; Invert order if you need the letter first
    db $08,$D6,$81 ; POINTER TO FLOOR # VARIABLE
    db $A9 ; FLOOR (F=9F)

org $18373
    db $AC ; BASEMENT (B=9B)
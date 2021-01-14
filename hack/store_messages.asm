arch 65816
lorom

;;
;; REMOVE "s" AND "et" AT THE END OF OBJECTS
;;
org $3FE7D
    db $0F,$00,$15
    db $08,$83,$83
    db $05,$0B,$FC
    db $88,$FE ; POINTER TO NEXT PHRASE
    ; db $C6 ; s
    db $05,$0B,$FA
    db $8D,$FE
    ; db $B8,$C7 ; et
    db $00,$05

;;
;; REMOVE "s." AT THE END OF CAN'T CARRY ANYMORE
;;
org $3B613
    ;db $C6,$D2 ; s.
    db $D2 ; .
    db $0A,$23,$B6
    db $00
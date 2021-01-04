arch 65816
lorom

;;
;; REMOVE "s" AND "et" AT THE END OF OBJECTS
;;
org $3FE7D
    db $0F,$00,$15
    db $08,$83,$83
    db $05,$0B,$FC
    db $89,$FE
    ; db $C6 ; s
    db $05,$0B,$FA
    db $90,$FE
    db $05,$0B,$FA
    db $90,$FE
    ; db $B8,$C7 ; et
    db $00,$00 ; FILL
    db $00
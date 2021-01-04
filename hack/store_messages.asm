arch 65816
lorom

;;
;; REMOVE S AT THE END OF OBJECTS
;;
org $3FE88
    ; db $C6 ; s
    db $05,$0B,$FA,$90,$FE
    db $FF


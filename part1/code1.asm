!!!M_START ..function.. (&a1&=1,&a2&=1,&a3&=1,&a4&=1,&a5&=1,&a6&=1,&a7&=1)
			<*you are in comment*>
			extern printf
			extern atoi
!!!M_FINISH
!!!M_START ..macro1.. (&a1&=1,&a2&=1,&a3&=1,&a4&=1,&a5&=1,&a6&=1,&a7&=1)
			<*for data section*>
			int: db '%d',&a1&,&a2&
!!!M_FINISH
!!!M_START ..macro2.. (&a1&=1,&a2&=1,&a3&=1,&a4&=1,&a5&=1,&a6&=1,&a7&=1)
			<*nested macro*>
			iteration:
					mov ebx,[n]
					cmp ebx,1
					je end
					add eax,ecx
					mov ecx,eax
					push eax
					push int
					call &a6
					jmp iteration
			!!!M_START ..macro3.. (&a1&=1,&a2&=1,&a3&=1,&a4&=1,&a5&=1,&a6&=1,&a7&=1)
						end:
						mov esp,ebp
						!!!M_START ..macro4.. (&a1&=1,&a2&=1,&a3&=1,&a4&=1,&a5&=1,&a6&=1,&a7&=1)
									pop ebp
									ret
						!!!M_FINISH
			!!!M_FINISH
!!!M_FINISH

..function.. ()

SECTION .data
	..macro1.. (10,0)

SECTION .bss
	i RESB 32
	n RESB 32
	S RESB 32

SECTION .text
	global main
main:
	push ebp
	mov ebp,esp
	mov ebx,dword[esp+12]
	mov ecx,[ebx+4]
	push ecx
	call atoi
	mov [n],eax

	mov eax,1
	mov [i],eax

	mov eax,0
	mov [S],eax
	push eax
	push int
	call printf
	add esp,8
	mov ecx,1
	..macro2.. ()
	..macro3.. ()

			extern printf
			extern atoi
SECTION .data
			int: db '%d',10,0
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
						end:
						mov esp,ebp
									pop ebp
									ret
						end:
						mov esp,ebp
									pop ebp
									ret
									pop ebp
									ret

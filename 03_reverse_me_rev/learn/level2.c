
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void no(void)
{
  printf("No\n");
  exit(0);
}

void ok(void)
{
  printf("Ok\n");
  exit(0);
}

int main(void)
{
  unsigned int uVar1;
  size_t sVar2;
  int iVar3;
  bool bVar4;
  char local_3d;
  char local_3c;
  char local_3b;
  char local_3a;
  char local_39 [24]; //input
  char local_21 [9]; //passwd
  unsigned int local_18;
  int local_14;
  int local_10;
  int local_c;
  
  local_c = 0;
  printf("Please enter key: ");
  local_10 = scanf("%s",local_39);
  if (local_10 != 1) {
    no();
  }
  if (local_39[1] != '0') {
    no();
  }
  if (local_39[0] != '0') {
    no();
  }
  // fflush(_stdin);
  memset(local_21,0,9);
  local_21[0] = 'd';
  local_3a = 0; // null terminator of local_3d
  local_18 = 2; // index of local_39 (input)
  local_14 = 1; // index of local_21 (password)
  while( true ) {
    sVar2 = strlen(local_21);
    uVar1 = local_18;
    bVar4 = false;
    if (sVar2 < 8) {
      sVar2 = strlen(local_39);
      bVar4 = uVar1 < sVar2;
    }
    if (!bVar4) break;
    local_3d = local_39[local_18];
    local_3c = local_39[local_18 + 1];
    local_3b = local_39[local_18 + 2];
    iVar3 = atoi(&local_3d);
    local_21[local_14] = (char)iVar3;
    local_18 = local_18 + 3;
    local_14 = local_14 + 1;
    //00e00l00a00b00e00r00e //false
    // e=101,l=108,a=97,b=98,e=101,r=114,e=101
    // 00 101 108 097 098 101 114 101
    // 00101108097098101114101

  }
  local_21[local_14] = '\0';
  iVar3 = strcmp(local_21,"delabere");
  if (iVar3 == 0) {
    ok();
  }
  else {
    no();
  }
  return 0;
}

#include "extcode.h"
#define __stdcall
#define __cdecl

#ifdef __cplusplus
extern "C" {
#endif

/*!
 * Returns a power of 2
 */
double __cdecl Power_of_2(double x);

MgErr __cdecl LVDLLStatus(char *errStr, int errStrLen, void *module);

void __cdecl SetExecuteVIsInPrivateExecutionSystem(Bool32 value);

#ifdef __cplusplus
} // extern "C"
#endif


// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_interface:msg/ImuData.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "custom_interface/msg/imu_data.h"


#ifndef CUSTOM_INTERFACE__MSG__DETAIL__IMU_DATA__STRUCT_H_
#define CUSTOM_INTERFACE__MSG__DETAIL__IMU_DATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/ImuData in the package custom_interface.
typedef struct custom_interface__msg__ImuData
{
  double roll;
  double pitch;
  double yaw;
} custom_interface__msg__ImuData;

// Struct for a sequence of custom_interface__msg__ImuData.
typedef struct custom_interface__msg__ImuData__Sequence
{
  custom_interface__msg__ImuData * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interface__msg__ImuData__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_INTERFACE__MSG__DETAIL__IMU_DATA__STRUCT_H_

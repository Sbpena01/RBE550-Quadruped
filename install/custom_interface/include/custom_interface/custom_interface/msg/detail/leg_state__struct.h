// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_interface:msg/LegState.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "custom_interface/msg/leg_state.h"


#ifndef CUSTOM_INTERFACE__MSG__DETAIL__LEG_STATE__STRUCT_H_
#define CUSTOM_INTERFACE__MSG__DETAIL__LEG_STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'pose'
#include "geometry_msgs/msg/detail/pose__struct.h"

/// Struct defined in msg/LegState in the package custom_interface.
typedef struct custom_interface__msg__LegState
{
  bool is_swing;
  geometry_msgs__msg__Pose pose;
} custom_interface__msg__LegState;

// Struct for a sequence of custom_interface__msg__LegState.
typedef struct custom_interface__msg__LegState__Sequence
{
  custom_interface__msg__LegState * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interface__msg__LegState__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_INTERFACE__MSG__DETAIL__LEG_STATE__STRUCT_H_

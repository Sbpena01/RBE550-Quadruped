// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from custom_interface:msg/LegState.idl
// generated code does not contain a copyright notice
#ifndef CUSTOM_INTERFACE__MSG__DETAIL__LEG_STATE__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define CUSTOM_INTERFACE__MSG__DETAIL__LEG_STATE__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "custom_interface/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "custom_interface/msg/detail/leg_state__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_custom_interface
bool cdr_serialize_custom_interface__msg__LegState(
  const custom_interface__msg__LegState * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_custom_interface
bool cdr_deserialize_custom_interface__msg__LegState(
  eprosima::fastcdr::Cdr &,
  custom_interface__msg__LegState * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_custom_interface
size_t get_serialized_size_custom_interface__msg__LegState(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_custom_interface
size_t max_serialized_size_custom_interface__msg__LegState(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_custom_interface
bool cdr_serialize_key_custom_interface__msg__LegState(
  const custom_interface__msg__LegState * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_custom_interface
size_t get_serialized_size_key_custom_interface__msg__LegState(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_custom_interface
size_t max_serialized_size_key_custom_interface__msg__LegState(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_custom_interface
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, custom_interface, msg, LegState)();

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_INTERFACE__MSG__DETAIL__LEG_STATE__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from custom_interface:msg/LegPose.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "custom_interface/msg/detail/leg_pose__functions.h"
#include "custom_interface/msg/detail/leg_pose__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace custom_interface
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void LegPose_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) custom_interface::msg::LegPose(_init);
}

void LegPose_fini_function(void * message_memory)
{
  auto typed_message = static_cast<custom_interface::msg::LegPose *>(message_memory);
  typed_message->~LegPose();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember LegPose_message_member_array[2] = {
  {
    "is_swing",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(custom_interface::msg::LegPose, is_swing),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "leg_pose",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<geometry_msgs::msg::Pose>(),  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(custom_interface::msg::LegPose, leg_pose),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers LegPose_message_members = {
  "custom_interface::msg",  // message namespace
  "LegPose",  // message name
  2,  // number of fields
  sizeof(custom_interface::msg::LegPose),
  false,  // has_any_key_member_
  LegPose_message_member_array,  // message members
  LegPose_init_function,  // function to initialize message memory (memory has to be allocated)
  LegPose_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t LegPose_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &LegPose_message_members,
  get_message_typesupport_handle_function,
  &custom_interface__msg__LegPose__get_type_hash,
  &custom_interface__msg__LegPose__get_type_description,
  &custom_interface__msg__LegPose__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace custom_interface


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<custom_interface::msg::LegPose>()
{
  return &::custom_interface::msg::rosidl_typesupport_introspection_cpp::LegPose_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, custom_interface, msg, LegPose)() {
  return &::custom_interface::msg::rosidl_typesupport_introspection_cpp::LegPose_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

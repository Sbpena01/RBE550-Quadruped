// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from custom_interface:msg/LegState.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "custom_interface/msg/leg_state.hpp"


#ifndef CUSTOM_INTERFACE__MSG__DETAIL__LEG_STATE__TRAITS_HPP_
#define CUSTOM_INTERFACE__MSG__DETAIL__LEG_STATE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "custom_interface/msg/detail/leg_state__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'pose'
#include "geometry_msgs/msg/detail/pose__traits.hpp"

namespace custom_interface
{

namespace msg
{

inline void to_flow_style_yaml(
  const LegState & msg,
  std::ostream & out)
{
  out << "{";
  // member: is_swing
  {
    out << "is_swing: ";
    rosidl_generator_traits::value_to_yaml(msg.is_swing, out);
    out << ", ";
  }

  // member: pose
  {
    out << "pose: ";
    to_flow_style_yaml(msg.pose, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const LegState & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: is_swing
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "is_swing: ";
    rosidl_generator_traits::value_to_yaml(msg.is_swing, out);
    out << "\n";
  }

  // member: pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pose:\n";
    to_block_style_yaml(msg.pose, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const LegState & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace custom_interface

namespace rosidl_generator_traits
{

[[deprecated("use custom_interface::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const custom_interface::msg::LegState & msg,
  std::ostream & out, size_t indentation = 0)
{
  custom_interface::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use custom_interface::msg::to_yaml() instead")]]
inline std::string to_yaml(const custom_interface::msg::LegState & msg)
{
  return custom_interface::msg::to_yaml(msg);
}

template<>
inline const char * data_type<custom_interface::msg::LegState>()
{
  return "custom_interface::msg::LegState";
}

template<>
inline const char * name<custom_interface::msg::LegState>()
{
  return "custom_interface/msg/LegState";
}

template<>
struct has_fixed_size<custom_interface::msg::LegState>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::Pose>::value> {};

template<>
struct has_bounded_size<custom_interface::msg::LegState>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::Pose>::value> {};

template<>
struct is_message<custom_interface::msg::LegState>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // CUSTOM_INTERFACE__MSG__DETAIL__LEG_STATE__TRAITS_HPP_

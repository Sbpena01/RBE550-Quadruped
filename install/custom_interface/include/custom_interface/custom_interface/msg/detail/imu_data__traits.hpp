// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from custom_interface:msg/ImuData.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "custom_interface/msg/imu_data.hpp"


#ifndef CUSTOM_INTERFACE__MSG__DETAIL__IMU_DATA__TRAITS_HPP_
#define CUSTOM_INTERFACE__MSG__DETAIL__IMU_DATA__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "custom_interface/msg/detail/imu_data__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace custom_interface
{

namespace msg
{

inline void to_flow_style_yaml(
  const ImuData & msg,
  std::ostream & out)
{
  out << "{";
  // member: roll
  {
    out << "roll: ";
    rosidl_generator_traits::value_to_yaml(msg.roll, out);
    out << ", ";
  }

  // member: pitch
  {
    out << "pitch: ";
    rosidl_generator_traits::value_to_yaml(msg.pitch, out);
    out << ", ";
  }

  // member: yaw
  {
    out << "yaw: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ImuData & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: roll
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "roll: ";
    rosidl_generator_traits::value_to_yaml(msg.roll, out);
    out << "\n";
  }

  // member: pitch
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pitch: ";
    rosidl_generator_traits::value_to_yaml(msg.pitch, out);
    out << "\n";
  }

  // member: yaw
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ImuData & msg, bool use_flow_style = false)
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
  const custom_interface::msg::ImuData & msg,
  std::ostream & out, size_t indentation = 0)
{
  custom_interface::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use custom_interface::msg::to_yaml() instead")]]
inline std::string to_yaml(const custom_interface::msg::ImuData & msg)
{
  return custom_interface::msg::to_yaml(msg);
}

template<>
inline const char * data_type<custom_interface::msg::ImuData>()
{
  return "custom_interface::msg::ImuData";
}

template<>
inline const char * name<custom_interface::msg::ImuData>()
{
  return "custom_interface/msg/ImuData";
}

template<>
struct has_fixed_size<custom_interface::msg::ImuData>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<custom_interface::msg::ImuData>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<custom_interface::msg::ImuData>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // CUSTOM_INTERFACE__MSG__DETAIL__IMU_DATA__TRAITS_HPP_

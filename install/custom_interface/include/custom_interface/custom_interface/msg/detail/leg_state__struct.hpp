// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from custom_interface:msg/LegState.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "custom_interface/msg/leg_state.hpp"


#ifndef CUSTOM_INTERFACE__MSG__DETAIL__LEG_STATE__STRUCT_HPP_
#define CUSTOM_INTERFACE__MSG__DETAIL__LEG_STATE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'pose'
#include "geometry_msgs/msg/detail/pose__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__custom_interface__msg__LegState __attribute__((deprecated))
#else
# define DEPRECATED__custom_interface__msg__LegState __declspec(deprecated)
#endif

namespace custom_interface
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct LegState_
{
  using Type = LegState_<ContainerAllocator>;

  explicit LegState_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pose(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_swing = false;
    }
  }

  explicit LegState_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pose(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_swing = false;
    }
  }

  // field types and members
  using _is_swing_type =
    bool;
  _is_swing_type is_swing;
  using _pose_type =
    geometry_msgs::msg::Pose_<ContainerAllocator>;
  _pose_type pose;

  // setters for named parameter idiom
  Type & set__is_swing(
    const bool & _arg)
  {
    this->is_swing = _arg;
    return *this;
  }
  Type & set__pose(
    const geometry_msgs::msg::Pose_<ContainerAllocator> & _arg)
  {
    this->pose = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    custom_interface::msg::LegState_<ContainerAllocator> *;
  using ConstRawPtr =
    const custom_interface::msg::LegState_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<custom_interface::msg::LegState_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<custom_interface::msg::LegState_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      custom_interface::msg::LegState_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<custom_interface::msg::LegState_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      custom_interface::msg::LegState_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<custom_interface::msg::LegState_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<custom_interface::msg::LegState_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<custom_interface::msg::LegState_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__custom_interface__msg__LegState
    std::shared_ptr<custom_interface::msg::LegState_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__custom_interface__msg__LegState
    std::shared_ptr<custom_interface::msg::LegState_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const LegState_ & other) const
  {
    if (this->is_swing != other.is_swing) {
      return false;
    }
    if (this->pose != other.pose) {
      return false;
    }
    return true;
  }
  bool operator!=(const LegState_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct LegState_

// alias to use template instance with default allocator
using LegState =
  custom_interface::msg::LegState_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace custom_interface

#endif  // CUSTOM_INTERFACE__MSG__DETAIL__LEG_STATE__STRUCT_HPP_

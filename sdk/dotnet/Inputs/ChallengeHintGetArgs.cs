// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ctfd.Inputs
{

    public sealed class ChallengeHintGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Content of the hint as displayed to the end-user.
        /// </summary>
        [Input("content", required: true)]
        public Input<string> Content { get; set; } = null!;

        /// <summary>
        /// Cost of the hint, and if any specified, the end-user will consume its own (or team) points to get it.
        /// </summary>
        [Input("cost")]
        public Input<int>? Cost { get; set; }

        /// <summary>
        /// Identifier of the hint, used internally to handle the CTFd corresponding object.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("requirements")]
        private InputList<string>? _requirements;

        /// <summary>
        /// Other hints required to be consumed before getting this one. Useful for cost-increasing hint strategies with more and more help.
        /// </summary>
        public InputList<string> Requirements
        {
            get => _requirements ?? (_requirements = new InputList<string>());
            set => _requirements = value;
        }

        public ChallengeHintGetArgs()
        {
        }
        public static new ChallengeHintGetArgs Empty => new ChallengeHintGetArgs();
    }
}
